import requests
import json


def load_secrets():
    with open("./secrets.json") as secrets_file:
        secrets = json.load(secrets_file)
    return secrets


def get_token():
    secrets = load_secrets()
    headers = {"content-type": "application/json"}
    data = {
        "client_id": secrets["clientId"],
        "client_secret": secrets["clientSecret"],
        "audience": "backend",
        "grant_type": "client_credentials",
    }
    response = requests.post(
        secrets["authUrl"], data=json.dumps(data), headers=headers)
    return json.loads(response.text).get("access_token")
