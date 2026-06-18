import pytest
from src.moltbot import Moltbot, User, Channel

def test_add_user():
    moltbot = Moltbot()
    user = User(id=1, name="John Doe", channel=Channel.WHATSAPP)
    moltbot.add_user(user)
    assert moltbot.get_user(1) == user

def test_get_user():
    moltbot = Moltbot()
    user = User(id=1, name="John Doe", channel=Channel.WHATSAPP)
    moltbot.add_user(user)
    assert moltbot.get_user(1) == user

def test_interact():
    moltbot = Moltbot()
    user = User(id=1, name="John Doe", channel=Channel.WHATSAPP)
    moltbot.add_user(user)
    response = moltbot.interact(1, "Hello, Moltbot!")
    assert response == "Hello, John Doe! You said: Hello, Moltbot!"

def test_to_json():
    moltbot = Moltbot()
    user = User(id=1, name="John Doe", channel=Channel.WHATSAPP)
    moltbot.add_user(user)
    json_str = moltbot.to_json()
    assert json_str == '{"1": {"name": "John Doe", "channel": "whatsapp"}}'

def test_from_json():
    json_str = '{"1": {"name": "John Doe", "channel": "whatsapp"}}'
    moltbot = Moltbot.from_json(json_str)
    user = moltbot.get_user(1)
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.channel == Channel.WHATSAPP

def test_interact_user_not_found():
    moltbot = Moltbot()
    response = moltbot.interact(1, "Hello, Moltbot!")
    assert response == "User not found"
