from pathlib import Path


ROOT = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_severity_and_blocking_contract_is_present() -> None:
    router = read("SKILL.md")

    assert "Major Concerns" in router
    assert "Minor Comments" in router
    assert "Blocking Yes" in router
    assert "Minor Comments are never blocking" in router
    assert "Do not impose a concern quota" in router


def test_reviewers_are_isolated_before_synthesis() -> None:
    router = read("SKILL.md")

    assert "genuinely separate context" in router
    assert "Freeze each individual report before comparing" in router
    assert "not shown to reviewers" in router
    assert "Do not let one reviewer read" in router


def test_traceability_and_non_invention_are_required() -> None:
    router = read("SKILL.md")

    assert "claim_pointer" in router
    assert "evidence_pointer" in router
    assert "Do not invent experiments" in router


def test_numerical_audit_follows_requested_scope() -> None:
    router = " ".join(read("SKILL.md").split())
    assert "only when the user requests a whole-manuscript review or identifies a specific table to check" in router
    assert "A section review or a passing table citation does not activate the audit" in router
    assert "check only the selected tables" in router


def test_punctuation_guard_is_part_of_the_reviewer_contract() -> None:
    router = read("SKILL.md")

    assert "Avoid em dashes, en dashes, and colons" in router
    assert "Do not use dash punctuation or colons" in router


def test_skill_is_venue_aware_and_policy_is_not_hardcoded() -> None:
    router = read("SKILL.md")

    assert "name: robotics-reviewer" in router
    assert "verify the current official" in router
    assert "Do not rely on memory" in router
    assert "generic rubric; venue policy unverified" in router


def test_robotics_and_ml_gates_cover_requested_risks() -> None:
    gates = read("references/domain-specific-review-gates.md")

    assert "Data leakage and contamination" in gates
    assert "Matched comparisons" in gates
    assert "Replication and statistical independence" in gates
    assert "Ablations and attribution" in gates
    assert "cross-embodiment" in gates
    assert "sim-to-real" in gates
    assert "control frequency" in gates
    assert "Failures and safety" in gates
    assert "Reproducibility" in gates
