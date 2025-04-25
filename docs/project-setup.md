# 🛠️ Project Setup Guide (for Development)

This guide is tailored for setting up this specific project on a new machine.

---

## 🧱 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/stukk.git
cd stukk
```

---

## 🐍 2. Create and activate a virtual environment

> Recommended: Use `venv` or any preferred environment manager.

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate
```

---

## 📦 3. Update pip, setuptools and install dependencies

```bash
python -m pip install --upgrade pip setuptools
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ✅ 4. Install and run `pre-commit`

```bash
# Install the pre-commit hook
pre-commit install

# (Optional) Update the hooks if necessary
pre-commit autoupdate

# Run checks on all files
pre-commit run --all-files
```

---

## 🧪 5. Install the package locally in editable mode

```bash
pip install -e .
```

---

## ⬆️ 6. Version bumping with `tbump`

This project uses [`tbump`](https://github.com/dmerejkowsky/tbump) to update version numbers across files.

```bash
# Normal usage (creates commit and tag automatically)
tbump NEW_VERSION

# Skip committing and tagging
tbump --only-patch NEW_VERSION
```

You're now ready to begin development!
