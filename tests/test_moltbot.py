from moltbot import Moltbot, MoltbotConfig

def test_install():
    config = MoltbotConfig(channel="WhatsApp", device_id="12345")
    moltbot = Moltbot(config)
    assert moltbot.install() == "Installed Moltbot on 12345"

def test_interact():
    config = MoltbotConfig(channel="Telegram", device_id="67890")
    moltbot = Moltbot(config)
    assert moltbot.interact("Hello, Moltbot!") == "Moltbot responded to Hello, Moltbot! on Telegram"

def test_invalid_channel():
    config = MoltbotConfig(channel="", device_id="12345")
    moltbot = Moltbot(config)
    assert moltbot.install() == "Installed Moltbot on 12345"
    assert moltbot.interact("Hello, Moltbot!") == "Moltbot responded to Hello, Moltbot! on "

def test_invalid_device_id():
    config = MoltbotConfig(channel="WhatsApp", device_id="")
    moltbot = Moltbot(config)
    assert moltbot.install() == "Installed Moltbot on "
    assert moltbot.interact("Hello, Moltbot!") == "Moltbot responded to Hello, Moltbot! on WhatsApp"
