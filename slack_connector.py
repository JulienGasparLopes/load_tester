import json
import sys
import requests
from helpers import load_secrets


class SlackConnector:
    def __init__(self, username="LoadTesterBot") -> None:
        secret = load_secrets()
        self._url = secret["slackWebHookUrl"]
        self.username = username

    def send_message(self, title, message, channel=None, icon_emoji="satellite"):
        # "channel": "#channel_name",
        slack_data = {
            "username": self.username,
            "attachments": [
                {
                    "color": "#9733EE",
                    "fields": [
                        {
                            "title": title,
                            "value": message,
                            "short": "false",
                        }
                    ]
                }
            ]
        }
        if channel:
            slack_data = slack_data | {"channel": channel}
        if icon_emoji:
            slack_data = slack_data | {"icon_emoji": f":{icon_emoji}:"}

        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json",
                   'Content-Length': byte_length}
        response = requests.post(
            self._url, data=json.dumps(slack_data), headers=headers)
        if code := response.status_code != 200:
            print(f"Error {code} while sending message : {response.text}")
