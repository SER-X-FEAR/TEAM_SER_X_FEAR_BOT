# CHANGES

All notable changes to this repository are recorded in this file.

2026-06-21
 
 - Changed: default logging level set to WARNING so only greeting prints on startup.

Notes:
- Local `.env` file must be created by the operator and MUST NOT be committed to the repository. The project `.gitignore` already ignores `.env`.

2026-06-21 (additional)
- Added: automatic virtual environment creation and dependency installation on first run (`src/team_ser_x_fear_bot/system/venv.py`).
- Behavior: if not running in the project's `.venv`, the bot will create `.venv`, install `requirements.txt` into it, and re-exec into that environment. Marker env `TSXFB_BOOTED=1` prevents loops.

