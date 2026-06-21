from __future__ import annotations

import logging
import os
from typing import Any

from .core import BotCore
from .system.logger import configure_logging


class TeamSerXFearBot(BotCore):
    def __init__(self) -> None:
        # configure package logging at INFO by default
        configure_logging()
        super().__init__(name="TEAM_SER_X_FEAR_BOT")

        # optional environment information; do not block startup if missing
        self.bot_token = os.getenv("BOT_TOKEN")
        self.highrise_api_url = os.getenv("HIGHRISE_API_URL")
        self.node_env = os.getenv("NODE_ENV", "development")

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Bot initialized in %s mode.", self.node_env)

    def run(self) -> None:
        # Start core which loads modules silently and prints greeting
        self.start()

    def send_highrise_request(self, endpoint: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self.logger.debug("Sending request to Highrise endpoint: %s", endpoint)
        # TODO: implement actual Highrise API interaction
        return {}
