import json

import requests

from Common.Config import Config

config = Config("../../config.ini")

session_id = "ab89a0f8-0194-4f9f-97dd-b7a19f38ad03"
url = "http://localhost:{}/query_session".format(config.SERVER_PORT)

# Data to be sent in POST request
payload = {
    "session_id": session_id
}

# Making POST request
response = requests.post(url, json=payload)
model = response.json()["model"]
pipeline = json.loads(model["pipeline"])
print(pipeline)
