from pathlib import Path

def system_health() -> dict:
    checks = {
        "repo_files": Path("README.md").exists(),
        "sample_data": Path("data/sample/btc_demo.csv").exists(),
        "tests_folder": Path("tests").exists(),
        "docs_folder": Path("docs").exists(),
    }
    return {
        "system": "T",
        "status": "ok" if all(checks.values()) else "degraded",
        "checks": checks,
        "mode": "research_only",
    }
