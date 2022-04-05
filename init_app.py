from genericpath import exists
import json


if __name__ == "__main__":
    if exists("./secrets.json"):
        print("App already configured. See secrets.json file")
    else:
        with open("./secrets.json", "x") as file:
            data = {
                "clientId": "",
                "clientSecret": "",
                "authUrl": "", "slackWebhookUrl": ""
            }
            file.write(json.dumps(data))
