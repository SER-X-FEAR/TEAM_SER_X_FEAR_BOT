from __future__ import annotations

import os

from .bot import TeamSerXFearBot
from .system.venv import ensure_venv_and_reexec


def main() -> None:
    # If not already booted inside the venv, ensure it and re-exec into it.
    if not os.environ.get("TSXFB_BOOTED"):
        ensure_venv_and_reexec(venv_dir=".venv", requirements="requirements.txt")

    bot = TeamSerXFearBot()
    bot.run()


if __name__ == "__main__":
    main()
