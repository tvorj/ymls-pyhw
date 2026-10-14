# Work in your repository and run tests locally

Use Git and CPython **3.13** for this release. Some tests inspect Python bytecode,
so using the same Python minor version matters. Download Python from
[python.org](https://www.python.org/downloads/) and Git from
[git-scm.com](https://git-scm.com/downloads) if needed.

## 1. Create your personal repository

The instructor supplies the shared course repository URL. Create an **empty**
repository in your own GitHub or GitLab account, using the visibility required by
the instructor. Do not initialize it with a README, license, or gitignore.
The school does not need to provision your repository.

In the commands below, replace `COURSE_REPOSITORY_URL` with the shared course URL
and `YOUR_REPOSITORY_URL` with your empty personal repository's URL. Do not type
the placeholder names literally.

```sh
git clone COURSE_REPOSITORY_URL python-homework
cd python-homework
git remote rename origin upstream
git remote add origin YOUR_REPOSITORY_URL
git remote -v
git push -u origin main
```

`upstream` points to the shared repository where new tasks appear. `origin`
points to your own repository where you save solutions. Only push to `origin`.
Use your hosting provider's Git authentication instructions if prompted.

Before your first commit, configure your Git author identity if it is not set:

```sh
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

All subsequent commands run from the repository root: the directory containing
this file, `requirements.txt`, and `pytest.ini`.

## 2. Create a virtual environment

### Linux and macOS

```sh
python3.13 --version
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -3.13 --version
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents activation, use the environment's Python directly; no
activation or execution-policy change is required:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest 01.1.PythonTools/tasks/hello_world/test_public.py -v
```

Use `.\.venv\Scripts\python.exe` instead of `python` in later Python commands
when following this alternative.

Verify the environment:

```sh
python --version
python -m pytest --version
python -c "import testlib; print(testlib.__file__)"
```

The Python version should be 3.13.x. The testlib path should point to this
repository's `tools/testlib/testlib` directory. Dependencies are installed once
per clone; activation must be repeated when you open a new terminal.

## 3. Read and implement one task

Start with `01.1.PythonTools/tasks/hello_world/README.md`. Implement the matching
`hello_world.py` file. Read the requirements before editing; preserve function
names, signatures, and docstrings. Edit the starter `.py` file rather than writing
the answer in a notebook or in `test_public.py`.

Run its supplied tests:

```sh
python -m pytest 01.1.PythonTools/tasks/hello_world/test_public.py -v
```

Before implementation, a failing assertion is expected: it confirms that pytest
can import and call your starter function. A collection/import error instead
means the environment or imports need attention. After implementation, the task
should pass. Next, repeat the workflow for `testlib_test`:

```sh
python -m pytest 01.1.PythonTools/tasks/testlib_test/test_public.py -v
```

For a core task:

```sh
python -m pytest 01.2.BasicTypes/tasks/reverse_list/test_public.py -v
```

In a failed test, read the function name, input, failing assertion, and actual
versus expected values. Fix the solution and run the same command again. Keep
the supplied tests intact; you may add your own separate tests for experimentation.

Useful commands:

```sh
# Stop at the first failure and show details.
python -m pytest 01.2.BasicTypes/tasks/reverse_list/test_public.py -x -vv

# Run only tests whose names contain reverse_iterative.
python -m pytest 01.2.BasicTypes/tasks/reverse_list/test_public.py -k reverse_iterative -v

# Collect every supplied test without executing student functions.
python -m pytest --collect-only -q

# Run all core tasks; unfinished tasks will fail.
python -m pytest 01.2.BasicTypes/tasks -q

# Run all released public tests, including the advanced group.
python -m pytest -q
```

Tests have a 60-second per-test timeout. An algorithm that hangs or exceeds that
limit needs investigation. Passing public tests does not guarantee all possible
inputs are handled or that a school grade has been recorded.

## 4. Save and push your solution

For the first task:

```sh
git status
git diff -- 01.1.PythonTools/tasks/hello_world/hello_world.py
git add 01.1.PythonTools/tasks/hello_world/hello_world.py
git commit -m "Implement hello_world"
git push origin main
```

Stage the solution file deliberately. Do not commit your virtual environment,
editor files, or generated caches. `.gitignore` excludes common generated files.
You can commit unfinished work too; describe it accurately in the commit message.

Check your personal repository in the browser to confirm the commit arrived.
Keep the repository URL and commit link available when the instructor requests
your work for review. Pushing is a backup and sharing operation in this setup;
there is no Manytask registration or automatic score reporting.

## 5. Receive later homework and corrections

First commit your current work and check that `git status` reports a clean
worktree. Then merge updates from the shared repository and push the result to
your personal repository:

```sh
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

New task directories will appear alongside existing tasks. If a correction touches
a solution file you already edited, Git may report a conflict. Open the named
file, reconcile the changes while preserving your work, remove conflict markers,
then `git add` that file and `git commit` to finish the merge. Ask the instructor
for help if unsure; do not discard your solutions to resolve a conflict.

If a release changes dependencies, rerun `python -m pip install -r requirements.txt`
in your virtual environment.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `python3.13` or `py -3.13` unavailable | Install Python 3.13 and reopen your terminal |
| `No module named pytest` or `testlib` | Activate this clone's `.venv` and reinstall `requirements.txt` |
| Cannot find a task or `requirements.txt` | Run from the repository root |
| Unknown timeout option / missing timeout plugin | Install the complete `requirements.txt` |
| A required-operation test fails | Check the task restrictions as well as the returned result |
| Wrong interpreter in the IDE | Select `.venv/bin/python` or `.venv/Scripts/python.exe` |
| Push is rejected | Confirm `origin` is your own repository, authentication works, and no remote changes are missing |

In your IDE, select this repository's virtual environment and keep the terminal's
working directory at the repository root. The terminal commands above remain
the reference workflow.

Reference documentation: [Python virtual environments](https://docs.python.org/3.13/library/venv.html)
and [pytest import modes](https://docs.pytest.org/en/stable/explanation/pythonpath.html).
