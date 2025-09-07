import requests
from config import Settings
from tor_proxy import enable_tor_proxy

class TelegramClient:
    def __init__(self):
        enable_tor_proxy()
        self.base_url = f"https://api.telegram.org/bot{Settings.BOT_TOKEN}"

    def fetch_video_file(self, file_id: str) -> bytes:
        resp = requests.get(f"{self.base_url}/getFile", params={'file_id': file_id})
        resp.raise_for_status()
        file_path = resp.json()['result']['file_path']
        video_url = f"https://api.telegram.org/file/bot{Settings.BOT_TOKEN}/{file_path}"
        video_resp = requests.get(video_url)
        video_resp.raise_for_status()
        return video_resp.content
      
