from __future__ import annotations

import logging


class CommandHandler:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.commands: dict[str, str] = {
            "help": "Show available commands",
            "status": "Show bot status",
        }

    def handle(self, command: str) -> str:
        self.logger.info("Received command: %s", command)
        if command == "help":
            return self.get_help()
        if command == "status":
            return self.get_status()
        return "Unknown command. Use 'help' to see available commands."

    def get_help(self) -> str:
        return "Available commands: " + ", ".join(self.commands.keys())

    def get_status(self) -> str:
        return "TEAM_SER_X FEAR BOT is running." + "\n" + "Commands: " + ", ".join(self.commands.keys())
