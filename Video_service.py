import os
from pathlib import Path
from telegram_client import TelegramClient

class VideoService:
    def __init__(self):
        self.client = TelegramClient()
        self.storage_dir = Path(__file__).parent.parent / 'videos'
        self.storage_dir.mkdir(exist_ok=True)

    def save_video(self, file_id: str) -> str:
        video_bytes = self.client.fetch_video_file(file_id)
        file_path = self.storage_dir / f"{file_id}.mp4"
        with open(file_path, 'wb') as f:
            f.write(video_bytes)
        return str(file_path)
      
