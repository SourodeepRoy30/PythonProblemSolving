# Python Dev Setup — Personal Reference Guide

---

## 1. Conda — Create & Manage Virtual Environments

### Create a new environment
```bash
conda create -n <env-name> python=3.11
```
Example:
```bash
conda create -n pyenv python=3.11
```

### Activate an environment
```bash
conda activate <env-name>
```

### Deactivate (exit) the environment
```bash
conda deactivate
```

### List all environments
```bash
conda env list
```

### Delete an environment
```bash
conda deactivate
conda env remove -n <env-name>
```

### Install packages inside an active environment
```bash
pip install <package-name>
```
Example:
```bash
pip install ipykernel jupyter numpy pandas
```

### Register environment as a Jupyter kernel (for .ipynb in VSCode)
```bash
python -m ipykernel install --user --name <env-name> --display-name "Python (<env-name>)"
```

---

## 2. requirements.txt — Save & Restore Dependencies

### Save all currently installed packages to requirements.txt
```bash
conda activate <env-name>
pip freeze > requirements.txt
```
> Run this after installing new packages to keep it up to date.

### Install all packages from requirements.txt (on a new machine or fresh env)
```bash
pip install -r requirements.txt
```

---

## 3. Link a Local Folder to a GitHub Repo

### Step 1 — Create repo on GitHub first
Go to github.com → New Repository → give it a name → Private → Create (don't add README yet)

### Step 2 — Navigate to your local folder
```bash
cd ~/Desktop/<your-folder-name>
```

### Step 3 — Initialise git and connect to GitHub
```bash
git init
git remote add origin https://github.com/<your-username>/<repo-name>.git
```

### Step 4 — Make your first commit and push
```bash
git add .
git commit -m "first commit"
git branch -M main
git push -u origin main
```
> The `-u` flag sets `origin main` as the default. After this, you can just type `git push`.

### Check if remote is connected correctly
```bash
git remote -v
```

---

## 4. Daily Git Workflow — Add, Commit, Push, Pull

### The standard end-of-session routine
```bash
git add .
git commit -m "describe what you did"
git push
```

### Pull latest changes from GitHub (e.g. if you edited on another machine)
```bash
git pull
```

### See what files have changed (before committing)
```bash
git status
```

### See your commit history
```bash
git log --oneline
```

### Add only a specific file (instead of everything)
```bash
git add path/to/file.py
```

---

## 5. Open Any Project in VSCode

```bash
cd ~/Desktop/<folder-name>
code .
```

## 6. Select Python Interpreter in VSCode

`Cmd+Shift+P` → type **Python: Select Interpreter** → pick your conda env

## 7. Select Jupyter Kernel in VSCode

Open any `.ipynb` file → click **Select Kernel** (top right) → pick your env

---

## Quick Reference Card

| Task | Command |
|---|---|
| Create env | `conda create -n <name> python=3.11` |
| Activate env | `conda activate <name>` |
| Deactivate | `conda deactivate` |
| List envs | `conda env list` |
| Delete env | `conda env remove -n <name>` |
| Install package | `pip install <package>` |
| Save dependencies | `pip freeze > requirements.txt` |
| Restore dependencies | `pip install -r requirements.txt` |
| Init git repo | `git init` |
| Link to GitHub | `git remote add origin <url>` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push` |
| Pull | `git pull` |
| Check status | `git status` |
| View history | `git log --oneline` |
| Open in VSCode | `code .` |
