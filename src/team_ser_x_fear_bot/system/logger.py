"""Simple logger configuration helper for the bot."""

import logging


def configure_logging(level: int = logging.WARNING) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
