import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict

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

    def add_user(self, user: User):
        self.users[user.id] = user

    def get_user(self, user_id: int) -> User:
        return self.users.get(user_id)

    def interact(self, user_id: int, message: str) -> str:
        user = self.get_user(user_id)
        if user:
            # Simulate interaction with Moltbot via the user's preferred channel
            return f"Hello, {user.name}! You said: {message}"
        else:
            return "User not found"

    def to_json(self) -> str:
        users_json = {user_id: {
            "name": user.name,
            "channel": user.channel.value
        } for user_id, user in self.users.items()}
        return json.dumps(users_json)

    @classmethod
    def from_json(cls, json_str: str) -> "Moltbot":
        moltbot = cls()
        users_json = json.loads(json_str)
        for user_id, user_data in users_json.items():
            user = User(
                id=int(user_id),
                name=user_data["name"],
                channel=Channel(user_data["channel"])
            )
            moltbot.add_user(user)
        return moltbot
