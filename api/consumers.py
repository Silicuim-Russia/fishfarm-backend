import os
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class StreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'hls_url': f"{os.getenv('HOST_URL', 'http://localhost:8000')}/media/stream.m3u8"
        }))
        await self.close()