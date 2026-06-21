from __future__ import annotations

import logging
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from team_ser_x_fear_bot.bot import TeamSerXFearBot


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    bot = TeamSerXFearBot()
    try:
        bot.run()
    except Exception as exc:
        logging.exception("Application error: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
