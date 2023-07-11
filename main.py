import requests
from json import load

with open("config.json", "r") as f:
    config = load(f)
token = config["token"]

def post_message(token, channel, content):
    url = f"https://discord.com:443/api/v9/channels/{channel}/messages"
    headers = {"Authorization": f"{token}", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36", "Content-Type": "application/json"}
    json={"content": f"{content}"}
    a = requests.post(url, headers=headers, json=json)
    print(a.status_code)

while 1:
    for i in token:
        for j in config["channels"]:
            for k in config["content_list"]:
                post_message(i,j,k)