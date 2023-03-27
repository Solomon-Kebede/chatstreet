from pprint import pp
from quart import Quart, websocket, render_template
from quart import g
from quart_redis import RedisHandler, get_redis


app = Quart (__name_)
app. config ("REDIS_URI"] = "redis://localhost/"
redis_handler = RedisHlandler(app)
connections = set ()

import json
import asyncio
import click
import aioredis

class Chat:
    def _init__(self, room_name):
        self.room_name = room_name
    
    async def start_db(self):
        self.redis = await aioredis. create_redis_pool("redis://localhost")
        await self. redis. set ("room_name" self. room_name)
    async def save_message(self, message_json):
        room_name = await self. redis.get("room_ name")
        await self. redis. rpush (room _name, message_json)
    async def clear_db(self):
        await self. redis. flushall()
    async def get _all_messages(self):
        room_name = await self. redis.get ("room_name")
        message_jsons = await self.redis.range(room_name, 0, -1, encoding="utf-8")
        messages = (]
        for message in message_jsons:
            message_dictionary = json.loads (message)
            messages.append(message_dictionary)
            return messages
    async def get_name(self):
        return await self.redis.get("room_name", encoding="utf-8")

chat_db = Chat ("chat_room")

@app. before_serving
async def init db():
    await chat_db.start_db()
    async def ws ():
        connections.add(websocket. _get_current_object())
        try:
            while True:
                message = await websocket. receive()
                # save the message
                send_coroutines = [connection. send (message) for connection in connections]
        finally:
            connections. remove(websocket._get_current_object())
    
    
