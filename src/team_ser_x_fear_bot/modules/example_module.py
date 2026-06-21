"""Example module for TEAM_SER_X_FEAR_BOT.

This module registers quietly and does not print anything on load.
"""


def register(bot) -> None:
    """Register module with the bot. Keep registration silent."""
    # Example: attach a help string or command handler to bot
    try:
        handlers = getattr(bot, "_module_handlers", {})
        handlers["example"] = lambda: "example module active"
        setattr(bot, "_module_handlers", handlers)
    except Exception:
        # Keep failures quiet; the core will log if debug enabled
        return
