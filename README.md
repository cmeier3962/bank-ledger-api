# your-project

A minimal Python package scaffold using the `src/` layout.

- Library code in `src/your_project/`
- Handy scripts in `scripts/`
- Installed locally in **editable mode** via `requirements.txt` (contains `-e .`)

## Repo layout

```
your-project/
├─ src/
│  └─ your_project/
│     ├─ __init__.py
│     └─ __main__.py
├─ scripts/
│  └─ smoke_test.py
├─ .gitignore
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

## Requirements
- Python 3.11+ (3.12/3.13 OK)

## Setup

```bash
# from repo root
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs the package in **editable** mode so changes under `src/your_project/` are picked up immediately.

## Quick check

Run the module:
```bash
python -m your_project
```

Run the smoke script:
```bash
python scripts/smoke_test.py
```

---

## Notes & rename steps

When you create a new project from this template:

1. Rename `src/your_project/` → `src/<new_pkg_name>/`
2. In files, replace `your_project` with `<new_pkg_name>`:
   - `pyproject.toml` (project name)
   - `scripts/smoke_test.py` import
   - `README.md` examples
   - `__main__.py` (optional)
3. Create venv, activate, and install:
   ```bash
   python -m venv .venv
   # activate...
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python -m <new_pkg_name>
   python scripts/smoke_test.py
   ```