# Modern Python Packaging Plan

Gold standard reference: [OpenSourceEconomics/dags](https://github.com/OpenSourceEconomics/dags)

## Items To Do

### 1. Clean up stale references and dead files

- `pyproject.toml`: Remove `pyfixest/` entries from `[tool.ruff.lint.per-file-ignores]`
- `pyproject.toml`: Remove `black` and `flake8` from `[project.optional-dependencies].dev`
- `.pre-commit-config.yaml`: Fix mypy hook `files: ^pyfixest/` → `^maketables/` (or `^src/maketables/` after layout change)
- Delete `MANIFEST.in` (not needed with hatchling)
- Delete stray files: `debug_model_types.py`, `pptx_first_version`, `database.db`, `README.html`, `objects.json`
- Delete generated directories: `__pycache__/`, `README_files/`, `latex_output/`, `output/`
- Add `__pycache__/`, `README_files/`, `latex_output/`, `output/`, `database.db`, `objects.json` to `.gitignore` if not already present

### 2. Fix Python version range and classifiers

- `requires-python = ">=3.10"`
- Add classifiers for 3.13, 3.14; remove 3.8, 3.9
- Update ruff `target-version` to `"py310"`

### 3. Switch to hatchling + hatch-vcs

Replace setuptools with hatchling and add git-tag-based dynamic versioning.

- Replace `[build-system]` with:
  ```toml
  [build-system]
  build-backend = "hatchling.build"
  requires = ["hatch-vcs", "hatchling"]
  ```
- Add `dynamic = ["version"]`, remove hardcoded `version = "0.1.7"`
- Add `[tool.hatch.version]` with `source = "vcs"`
- Add `[tool.hatch.build.hooks.vcs]` to generate `_version.py`
- Add `[tool.hatch.build.targets.sdist]` and `[tool.hatch.build.targets.wheel]` sections
- Remove `[tool.setuptools.packages.find]` section
- Add `_version.py` to `.gitignore`

### 4. Switch to `src/` layout

Move `maketables/` → `src/maketables/`.

- Move directory
- Update hatch build targets: `only-include = ["src"]`, `sources = ["src"]`
- Update pixi editable install path
- Update pytest `pythonpath` if needed

### 5. Add `py.typed` marker

Create empty `src/maketables/py.typed` (PEP 561).

### 6. Add `frozen: true` to pixi in CI

Update `.github/workflows/tests.yml` pixi setup to use `frozen: true`.

### 7. Add automated PyPI publish workflow

New file: `.github/workflows/publish-to-pypi.yml`

- Build sdist + wheel on every push
- Publish to PyPI only on tag push via `pypa/gh-action-pypi-publish`

### 8. Add dependabot.yml

New file: `.github/dependabot.yml` — monthly updates for GitHub Actions, grouped into single PR.

## Suggested Implementation Order

1. Clean up stale references and dead files (#1)
2. Fix Python version range (#2)
3. Switch to hatchling + hatch-vcs (#3)
4. Switch to `src/` layout (#4)
5. Add `py.typed` (#5)
6. Add `frozen: true` in CI (#6)
7. Add publish workflow (#7)
8. Add dependabot (#8)
