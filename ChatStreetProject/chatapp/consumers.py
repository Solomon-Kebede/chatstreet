# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        client = text_data_json.get("client")
        timestamp = text_data_json.get("timestamp")
        message_type = text_data_json.get("messageType")
        chatroom = text_data_json.get("chatroom")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
            "type": "chat_message",
            "message": message,
            "client": client,
            "timestamp": timestamp,
            "messageType": message_type,
            "chatroom": chatroom,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event.get("message")
        client = event.get("client")
        timestamp = event.get("timestamp")
        message_type = event.get("messageType")
        chatroom = event.get("chatroom")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "client": client,
            'timestamp': timestamp,
            "messageType": message_type,
            "chatroom": chatroom,
            }))