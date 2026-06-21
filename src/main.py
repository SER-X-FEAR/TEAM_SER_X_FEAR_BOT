from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / '.env'

load_dotenv(dotenv_path=ENV_PATH)

BOT_TOKEN = os.getenv('BOT_TOKEN')
HIGHRISE_API_URL = os.getenv('HIGHRISE_API_URL')

if not BOT_TOKEN or not HIGHRISE_API_URL:
    print('Missing required environment variables. Create a .env file from .env.example.', file=sys.stderr)
    sys.exit(1)


def start_bot() -> None:
    print('TEAM_SER_X FEAR BOT is starting...')
    print(f'Highrise API: {HIGHRISE_API_URL}')
    # TODO: add bot initialization and command handlers here


if __name__ == '__main__':
    start_bot()
