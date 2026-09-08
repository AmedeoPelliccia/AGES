from pathlib import Path
import re, subprocess, json, tempfile, math, textwrap, sys

src = Path("/mnt/data/Pegado text(20260908-111350).txt")
code = src.read_text(encoding="utf-8")

# Version bump and import.
code = code.replace('import json\nimport sys\n', 'import json\nimport math\nimport sys\n')
code = code.replace('ENGINE_VERSION = "0.1.0"', 'ENGINE_VERSION = "0.1.1"')

# Clarify anonymous entity identity policy in the module docstring.
code = code.replace(
'''- implementation-neutral: a neural/symbolic/hybrid kernel can replace the
  default structured kernel without changing the external contract.
''',
'''- implementation-neutral: a neural/symbolic/hybrid kernel can replace the
  default structured kernel without changing the external contract;
- conservative co-reference: entities without an explicit `id` are scoped to
  their source observation. Cross-observation entity fusion therefore requires
  a shared explicit identity anchor; the reference kernel never assumes that
  two anonymous observations denote the same real-world entity.
'''
)

# Add finite-JSON validation.
needle = '''def _optional_string(value: Any, path: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise GENIUSSError(f"{path} must be a non-empty string or null")
    return value.strip()


# ---------------------------------------------------------------------------
# Observation model
'''
replacement = '''def _optional_string(value: Any, path: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise GENIUSSError(f"{path} must be a non-empty string or null")
    return value.strip()


def _validate_finite_json(value: Any, path: str = "input") -> None:
    """Reject non-finite numbers and non-JSON values with a precise path."""
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise GENIUSSError(f"{path} must contain only finite numbers")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise GENIUSSError(f"{path} object keys must be strings")
            _validate_finite_json(child, f"{path}.{key}")
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        for index, child in enumerate(value):
            _validate_finite_json(child, f"{path}[{index}]")
        return
    raise GENIUSSError(
        f"{path} contains unsupported non-JSON value of type "
        f"{type(value).__name__}"
    )


# ---------------------------------------------------------------------------
# Observation model
'''
if needle not in code:
    raise RuntimeError("validation insertion point not found")
code = code.replace(needle, replacement)

# Validate programmatic API input as well as CLI input.
needle = '''    def integrate(self, document: Mapping[str, Any]) -> Json:
        observations_raw = document.get("observations")
'''
replacement = '''    def integrate(self, document: Mapping[str, Any]) -> Json:
        _validate_finite_json(document)
        observations_raw = document.get("observations")
'''
if needle not in code:
    raise RuntimeError("integrate insertion point not found")
code = code.replace(needle, replacement)

# Replace merge algorithm: semantic identity vs epistemic evidence.
start = code.index('    @staticmethod\n    def _merge_items(')
end = code.index('\n\n\n# ---------------------------------------------------------------------------\n# CLI', start)

new_merge = r'''    @staticmethod
    def _merge_items(
        items: list[Json],
        identity_key: str,
        provenance_key: str,
    ) -> list[Json]:
        """
        Merge items sharing an identity while distinguishing corroboration
        from semantic conflict.

        Epistemic fields (`confidence`, `salience`, provenance) do not define
        semantic disagreement. If two independent observations assert the
        same semantic core with different confidence/salience, the result is
        `corroborated`, provenance is united, and per-source epistemic evidence
        plus value ranges are retained without inventing an aggregate score.

        `conflicted` is reserved for materially different semantic cores that
        claim the same identity.
        """
        grouped: dict[str, list[Json]] = {}
        for item in items:
            grouped.setdefault(str(item[identity_key]), []).append(item)

        merged: list[Json] = []

        for item_id in sorted(grouped):
            group = grouped[item_id]
            if len(group) == 1:
                merged.append(group[0])
                continue

            epistemic_keys = {provenance_key, "confidence", "salience"}

            def semantic_core(item: Mapping[str, Any]) -> Json:
                return {
                    k: v
                    for k, v in item.items()
                    if k not in epistemic_keys
                }

            semantic_variants: dict[str, list[Json]] = {}
            for item in group:
                semantic_variants.setdefault(
                    canonical_json(semantic_core(item)), []
                ).append(item)

            if len(semantic_variants) == 1:
                base = semantic_core(group[0])

                provenance: list[str] = []
                epistemic_evidence: list[Json] = []
                confidence_values: list[float] = []
                salience_values: list[float] = []

                for item in group:
                    item_provenance = list(item.get(provenance_key, []))
                    provenance.extend(item_provenance)

                    evidence: Json = {
                        provenance_key: _sorted_unique(item_provenance)
                    }
                    if "confidence" in item:
                        confidence = float(item["confidence"])
                        confidence_values.append(confidence)
                        evidence["confidence"] = confidence
                    if "salience" in item:
                        salience = float(item["salience"])
                        salience_values.append(salience)
                        evidence["salience"] = salience
                    epistemic_evidence.append(evidence)

                base[provenance_key] = _sorted_unique(provenance)
                base["status"] = "corroborated"
                base["epistemicEvidence"] = sorted(
                    epistemic_evidence, key=canonical_json
                )

                if confidence_values:
                    unique_confidence = sorted(set(confidence_values))
                    if len(unique_confidence) == 1:
                        base["confidence"] = unique_confidence[0]
                    else:
                        base["confidenceRange"] = {
                            "min": min(unique_confidence),
                            "max": max(unique_confidence),
                        }

                if salience_values:
                    unique_salience = sorted(set(salience_values))
                    if len(unique_salience) == 1:
                        base["salience"] = unique_salience[0]
                    else:
                        base["salienceRange"] = {
                            "min": min(unique_salience),
                            "max": max(unique_salience),
                        }

                merged.append(base)
                continue

            # Same claimed identity, materially different semantic content.
            # Preserve every variant; do not select or average a winner.
            conflict_id = stable_id(
                "CONFLICT",
                [
                    semantic_core(item)
                    for item in sorted(group, key=canonical_json)
                ],
            )
            merged.append(
                {
                    "id": item_id,
                    "status": "conflicted",
                    "conflictId": conflict_id,
                    "variants": sorted(group, key=canonical_json),
                }
            )

        return merged
'''
code = code[:start] + new_merge + code[end:]

# Reject NaN/Infinity at JSON parsing time with a clean domain error.
old = '''    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise GENIUSSError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
'''
new = '''    def reject_nonfinite(token: str) -> None:
        raise GENIUSSError(
            f"invalid JSON numeric constant {token!r}; "
            "only finite JSON numbers are permitted"
        )

    try:
        value = json.loads(raw, parse_constant=reject_nonfinite)
    except json.JSONDecodeError as exc:
        raise GENIUSSError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
'''
if old not in code:
    raise RuntimeError("read_document replacement point not found")
code = code.replace(old, new)

out = Path("/mnt/data/geniuss_v0_1_1.py")
out.write_text(code, encoding="utf-8", newline="\n")

# Compile check.
compile(code, str(out), "exec")

def run(args, stdin=None):
    return subprocess.run(
        [sys.executable, str(out), *args],
        input=stdin,
        text=True,
        capture_output=True,
    )

results = []

# 1 self-test
r = run(["--self-test"])
results.append(("self-test", r.returncode == 0, r.stdout.strip() or r.stderr.strip()))

# 2 non-finite constants: clean failures, no traceback
for token in ("NaN", "Infinity", "-Infinity"):
    raw = '{"observations":[{"observationId":"O1","payload":{"x":%s}}]}' % token
    r = run(["-"], stdin=raw)
    ok = r.returncode == 1 and "[FAIL]" in r.stderr and "Traceback" not in r.stderr
    results.append((f"reject {token}", ok, r.stderr.strip()))

# 3 relation corroboration
relation_doc = {
    "observations": [
        {"observationId": "O1", "confidence": 0.97,
         "payload": {"relations": [{"source": "A", "predicate": "in", "target": "B"}]}},
        {"observationId": "O2", "confidence": 0.90,
         "payload": {"relations": [{"source": "A", "predicate": "in", "target": "B"}]}},
    ]
}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
    json.dump(relation_doc, f)
    relation_path = f.name
r = run([relation_path])
rel_out = json.loads(r.stdout)
rel = rel_out["relations"][0]
ok = (
    r.returncode == 0
    and rel["status"] == "corroborated"
    and rel["derivedFrom"] == ["O1", "O2"]
    and rel["confidenceRange"] == {"min": 0.9, "max": 0.97}
    and len(rel["epistemicEvidence"]) == 2
)
results.append(("relation corroboration", ok, json.dumps(rel, sort_keys=True)))

# 4 hypothesis corroboration
hyp_doc = {
    "observations": [
        {"observationId": "O1", "payload": {"hypotheses": [
            {"statement": "thermal degradation", "confidence": 0.7}]}},
        {"observationId": "O2", "payload": {"hypotheses": [
            {"statement": "thermal degradation", "confidence": 0.8}]}},
    ]
}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
    json.dump(hyp_doc, f)
    hyp_path = f.name
r = run([hyp_path])
hyp = json.loads(r.stdout)["hypotheses"][0]
ok = (
    r.returncode == 0
    and hyp["status"] == "corroborated"
    and hyp["supportedBy"] == ["O1", "O2"]
    and hyp["confidenceRange"] == {"min": 0.7, "max": 0.8}
)
results.append(("hypothesis corroboration", ok, json.dumps(hyp, sort_keys=True)))

# 5 true conflict: explicit same entity ID with materially different attributes
conflict_doc = {
    "observations": [
        {"observationId": "O1", "payload": {"entities": [
            {"id": "valve-A", "type": "valve", "attributes": {"state": "open"}}]}},
        {"observationId": "O2", "payload": {"entities": [
            {"id": "valve-A", "type": "valve", "attributes": {"state": "closed"}}]}},
    ]
}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
    json.dump(conflict_doc, f)
    conflict_path = f.name
r = run([conflict_path])
conf = json.loads(r.stdout)["entities"][0]
results.append(("material conflict", r.returncode == 0 and conf["status"] == "conflicted",
                json.dumps(conf, sort_keys=True)))

# 6 conservative anonymous entity identity: remains two entities
anon_doc = {
    "observations": [
        {"observationId": "O1", "payload": {"entities": [
            {"type": "valve", "attributes": {"state": "open"}}]}},
        {"observationId": "O2", "payload": {"entities": [
            {"type": "valve", "attributes": {"state": "open"}}]}},
    ]
}
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
    json.dump(anon_doc, f)
    anon_path = f.name
r = run([anon_path])
ents = json.loads(r.stdout)["entities"]
results.append(("anonymous entities remain distinct", r.returncode == 0 and len(ents) == 2,
                ",".join(e["id"] for e in ents)))

# 7 cross-process determinism
r1 = run([relation_path])
r2 = run([relation_path])
results.append(("cross-process determinism", r1.returncode == r2.returncode == 0 and r1.stdout == r2.stdout,
                "byte-identical" if r1.stdout == r2.stdout else "DIFF"))

passed = sum(ok for _, ok, _ in results)
print(f"Created {out} ({out.stat().st_size} bytes); compile=OK")
print(f"Tests: {passed}/{len(results)} passed")
for name, ok, detail in results:
    print(f"{'[OK]' if ok else '[FAIL]'} {name}: {detail[:300]}")
