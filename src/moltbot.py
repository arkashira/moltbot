import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class Channel(Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"

@dataclass
class User:
    id: int
    name: str
    channel: Channel

class Moltbot:
    def __init__(self):
        self.users = {}

    def install(self, user_id: int, name: str, channel: Channel):
        self.users[user_id] = User(id=user_id, name=name, channel=channel)
        return f"User {name} installed on {channel.value}"

    def interact(self, user_id: int, message: str):
        if user_id not in self.users:
            raise ValueError("User not found")
        user = self.users[user_id]
        return f"User {user.name} received message on {user.channel.value}: {message}"

    def setup(self, user_id: int, channel: Channel):
        if user_id not in self.users:
            raise ValueError("User not found")
        self.users[user_id].channel = channel
        return f"User {self.users[user_id].name} setup on {channel.value}"
