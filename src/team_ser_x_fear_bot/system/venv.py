from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


def _venv_python(venv_path: Path) -> Path:
    if os.name == "nt":
        return venv_path / "Scripts" / "python.exe"
    return venv_path / "bin" / "python"


def ensure_venv_and_reexec(venv_dir: str = ".venv", requirements: str = "requirements.txt") -> Optional[None]:
    """Ensure a virtual environment exists at `venv_dir`, install requirements and re-exec into it.

    If already running inside the target venv, returns None and does nothing.
    Otherwise creates venv (if missing), installs requirements, sets marker env and re-execs.
    """
    venv_path = Path(venv_dir).resolve()

    # Detect current venv: check VIRTUAL_ENV or sys.prefix
    venv_env = os.environ.get("VIRTUAL_ENV")
    try:
        cur_prefix = Path(sys.prefix).resolve()
    except Exception:
        cur_prefix = None

    if venv_env and Path(venv_env).resolve() == venv_path:
        return None
    if cur_prefix and cur_prefix == venv_path:
        return None

    # Create venv if missing
    if not venv_path.exists():
        subprocess.check_call([sys.executable, "-m", "venv", str(venv_path)])

    venv_py = _venv_python(venv_path)
    if not venv_py.exists():
        raise RuntimeError(f"Virtualenv python not found at {venv_py}")

    # Install requirements if the file exists
    req_file = Path(requirements)
    if req_file.exists():
        subprocess.check_call([str(venv_py), "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([str(venv_py), "-m", "pip", "install", "-r", str(req_file)])

    # Install the current package in editable mode into the venv so `-m team_ser_x_fear_bot` works
    project_root = Path.cwd()
    if (project_root / 'pyproject.toml').exists() or (project_root / 'setup.py').exists():
        subprocess.check_call([str(venv_py), "-m", "pip", "install", "-e", str(project_root)])

    # Re-exec into venv with a marker to avoid loops
    new_env = os.environ.copy()
    new_env["TSXFB_BOOTED"] = "1"
    os.execvpe(str(venv_py), [str(venv_py), "-m", "team_ser_x_fear_bot"], new_env)
