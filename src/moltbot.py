import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class MoltbotConfig:
    channel: str
    device_id: str

class Moltbot:
    def __init__(self, config: MoltbotConfig):
        self.config = config

    def install(self):
        # Simulate installation
        return f"Installed Moltbot on {self.config.device_id}"

    def interact(self, message: str):
        # Simulate interaction
        return f"Moltbot responded to {message} on {self.config.channel}"

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--channel", help="Preferred channel (e.g. WhatsApp, Telegram)")
    parser.add_argument("--device-id", help="Device ID")
    return parser.parse_args()

def main():
    args = parse_args()
    config = MoltbotConfig(channel=args.channel, device_id=args.device_id)
    moltbot = Moltbot(config)
    print(moltbot.install())
    print(moltbot.interact("Hello, Moltbot!"))

if __name__ == "__main__":
    main()
