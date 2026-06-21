from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from .commands import CommandHandler

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_ENV_PATH = Path.cwd() / ".env"
PACKAGE_ENV_PATH = PROJECT_ROOT / ".env"


def load_environment() -> None:
    env_path = DEFAULT_ENV_PATH if DEFAULT_ENV_PATH.exists() else PACKAGE_ENV_PATH
    load_dotenv(dotenv_path=env_path)


class TeamSerXFearBot:
    def __init__(self) -> None:
        load_environment()
        self.bot_token = os.getenv("BOT_TOKEN")
        self.highrise_api_url = os.getenv("HIGHRISE_API_URL")
        self.node_env = os.getenv("NODE_ENV", "development")

        if not self.bot_token or not self.highrise_api_url:
            raise RuntimeError(
                "Missing required environment variables. Create a .env file from .env.example."
            )

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Bot initialized in %s mode.", self.node_env)
        self.commands = CommandHandler()

    def run(self) -> None:
        self.logger.info("Starting TEAM_SER_X FEAR BOT...")
        self.logger.info("Highrise API: %s", self.highrise_api_url)
        self.logger.info("Bot token is loaded.")
        self.initialize_commands()
        self.logger.info("Bot is ready.")

    def initialize_commands(self) -> None:
        self.logger.info("Initializing command handlers...")
        reply = self.commands.handle("help")
        self.logger.info("Command output: %s", reply)

    def send_highrise_request(self, endpoint: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self.logger.debug("Sending request to Highrise endpoint: %s", endpoint)
        # TODO: implement actual Highrise API interaction
        return {}
