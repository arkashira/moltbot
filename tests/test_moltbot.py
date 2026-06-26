from moltbot import Moltbot, Channel

def test_install():
    moltbot = Moltbot()
    result = moltbot.install(1, "John Doe", Channel.WHATSAPP)
    assert result == "User John Doe installed on whatsapp"

def test_interact():
    moltbot = Moltbot()
    moltbot.install(1, "John Doe", Channel.WHATSAPP)
    result = moltbot.interact(1, "Hello, Moltbot!")
    assert result == "User John Doe received message on whatsapp: Hello, Moltbot!"

def test_setup():
    moltbot = Moltbot()
    moltbot.install(1, "John Doe", Channel.WHATSAPP)
    result = moltbot.setup(1, Channel.TELEGRAM)
    assert result == "User John Doe setup on telegram"

def test_interact_user_not_found():
    moltbot = Moltbot()
    try:
        moltbot.interact(1, "Hello, Moltbot!")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "User not found"

def test_setup_user_not_found():
    moltbot = Moltbot()
    try:
        moltbot.setup(1, Channel.TELEGRAM)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "User not found"
