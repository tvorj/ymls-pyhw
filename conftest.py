"""Make task modules importable when collecting several public test files."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for tasks_dir in sorted(ROOT.glob("[0-9]*.*/tasks")):
    for task_dir in sorted(tasks_dir.iterdir()):
        if task_dir.is_dir():
            sys.path.insert(0, str(task_dir))
