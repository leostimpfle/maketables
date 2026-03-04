# Future Improvements (not blocking release)

Items deferred from the initial modernization effort. Open as a GitHub issue for tracking.

## Ruff rules
Consider switching from cherry-picked rule groups to `select = ["ALL"]` with a small ignore list (like dags). Catches more issues but requires an initial cleanup pass.

## Type checker
Currently using mypy via pre-commit. Consider switching to [ty](https://github.com/astral-sh/ty) (Astral's type checker) with all rules set to error, as dags does.

## CI test matrix
Currently tests only on Windows + Python 3.13. Expand to multi-OS (ubuntu-latest, macos-latest, windows-latest) × multi-Python (3.10–3.14) matrix.

## Codecov integration
Add pytest-cov reporting in CI and upload to Codecov. Add `codecov.yml` with target thresholds and `.coveragerc` with appropriate exclusions.

## Enhanced pre-commit hooks
Add hooks from dags:
- `pyproject-fmt` — auto-formats pyproject.toml
- `no-commit-to-branch` — prevents direct commits to main
- `nbstripout` — strip notebook outputs
- `yamlfix` + `yamllint` — YAML hygiene
- `mdformat` — markdown formatting
- Additional standard hooks: `check-ast`, `check-case-conflict`, `check-docstring-first`, `check-merge-conflict`, `check-vcs-permalinks`, `fix-byte-order-marker`, `mixed-line-ending`
- `ci.autoupdate_schedule: monthly`

## GitHub issue and PR templates
Add:
- `.github/ISSUE_TEMPLATE/bug-report.md`
- `.github/ISSUE_TEMPLATE/feature-request.md`
- `.github/PULL_REQUEST_TEMPLATE.md`

## Pixi per-Python-version environments
Add `py310`, `py311`, `py312`, `py313` pixi environments for the CI matrix (in addition to existing feature-based environments).
