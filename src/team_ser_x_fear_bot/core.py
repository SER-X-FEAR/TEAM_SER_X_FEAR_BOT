from __future__ import annotations

import importlib
import logging
import pkgutil
from pathlib import Path
from typing import List


class BotCore:
    """Lightweight bot core that discovers and loads modules silently."""

    def __init__(self, name: str = "TEAM_SER_X_FEAR_BOT") -> None:
        self.name = name
        self.logger = logging.getLogger(self.__class__.__name__)
        self.modules: List[str] = []

    def discover_and_load_modules(self, package: str = "team_ser_x_fear_bot.modules") -> None:
        """Discover modules in the given package and call their `register(bot)` if present.

        Modules are loaded quietly: successful loads are logged at DEBUG level only.
        """
        try:
            pkg = importlib.import_module(package)
        except Exception:
            self.logger.debug("Modules package '%s' not found", package)
            return

        pkgpath = Path(pkg.__file__).parent
        for finder, modname, ispkg in pkgutil.iter_modules([str(pkgpath)]):
            try:
                mod = importlib.import_module(f"{package}.{modname}")
                if hasattr(mod, "register"):
                    mod.register(self)
                    self.modules.append(modname)
                    self.logger.debug("Loaded module: %s", modname)
            except Exception:
                self.logger.exception("Failed loading module %s", modname)

    def start(self) -> None:
        """Start the bot: load modules silently and print the minimal greeting."""
        # Discover and register modules quietly
        self.discover_and_load_modules()

        # Only print a brief greeting and that the bot started.
        print("Привет! Бот запущен.")
