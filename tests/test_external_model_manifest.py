import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_external_model_manifest_has_explicit_pipeline_components() -> None:
    manifest = json.loads((ROOT / "configs/external_models.json").read_text())
    required = {
        "id",
        "method",
        "site_information",
        "site_engine",
        "pose_engine",
        "scoring_engine",
        "refinement",
        "family",
    }
    arms = manifest["pipeline_arms"]

    assert len({arm["id"] for arm in arms}) == len(arms)
    assert all(required <= arm.keys() for arm in arms)
    assert {arm["site_information"] for arm in arms} <= {"pocket_supplied", "blind_site"}
    assert {arm["family"] for arm in arms} <= {"Classical", "Hybrid", "DL"}


def test_primary_comparison_is_supplied_pocket_only() -> None:
    manifest = json.loads((ROOT / "configs/external_models.json").read_text())

    assert manifest["comparison_scope"] == "supplied_pocket_only"

    primary = [arm for arm in manifest["pipeline_arms"] if arm.get("primary_comparison", True)]
    excluded = [arm for arm in manifest["pipeline_arms"] if not arm.get("primary_comparison", True)]

    assert primary
    assert all(arm["site_information"] == "pocket_supplied" for arm in primary)
    assert all(arm.get("exclusion_reason") for arm in excluded)


def test_external_model_family_is_derived_from_runtime_components() -> None:
    manifest = json.loads((ROOT / "configs/external_models.json").read_text())

    for arm in manifest["pipeline_arms"]:
        learned = (
            arm["site_engine"] in {"learned_pocket_prediction", "joint_learned_pose"}
            or arm["pose_engine"].startswith("learned_")
            or arm["scoring_engine"].startswith("learned_")
            or arm["refinement"] == "learned_refinement"
        )
        explicit_nonlearned_runtime = (
            arm["pose_engine"] == "classical_search"
            or arm["scoring_engine"] == "classical_energy"
            or arm["refinement"]
            in {"geometry_projection", "classical_minimization", "in_repo_physical_gradient"}
        )

        if arm["family"] == "Classical":
            assert not learned, arm["id"]
        elif arm["family"] == "DL":
            assert learned and not explicit_nonlearned_runtime, arm["id"]
        else:
            assert learned and explicit_nonlearned_runtime, arm["id"]


def test_external_model_sources_and_install_sets_are_pinned() -> None:
    manifest = json.loads((ROOT / "configs/external_models.json").read_text())
    default_targets = set(manifest["install_targets"])
    optional_targets = set(manifest["optional_install_targets"])

    assert default_targets.isdisjoint(optional_targets)
    assert "posebench-diffdock" not in default_targets
    assert "posebench-fabind" not in default_targets
    assert "posebench-dynamicbind" not in default_targets
    assert "posebench-flowdock" not in default_targets
    assert "posebench-diffdock" in optional_targets
    assert "posebench-fabind" in optional_targets
    assert "posebench-dynamicbind" in optional_targets
    assert "posebench-flowdock" in optional_targets
    for source in manifest["sources"].values():
        assert source["url"].startswith("https://")
        assert len(source["commit"]) == 40
        int(source["commit"], 16)


def test_cuda_build_compatibility_is_explicitly_pinned() -> None:
    manifest = json.loads((ROOT / "configs/external_models.json").read_text())
    override = manifest["environment_compatibility_overrides"]["posebench-diffdock"][0]

    assert set(override["packages"]) == {"gcc_linux-64", "gxx_linux-64"}
    assert override["version"] == "11"
    assert override["resolved_distribution"] == "conda-forge"
