import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    BOT_API_ID = os.getenv('BOT_API_ID')
    TELEGRAM_DB_URI = os.getenv('TELEGRAM_DB_URI')
    TOR_SOCKS_PORT = int(os.getenv('TOR_SOCKS_PORT', 9050))
    MEDHUB_DOMAIN = os.getenv('MEDHUB_DOMAIN', 'medhub.local')
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
