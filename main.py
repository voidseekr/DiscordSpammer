import requests
from json import load
from content_list import content_list
from random import choice

with open("config.json", "r") as f:
    config = load(f)
token = config["token"]

if not content_list:
    content_list = config["content_list"]

def post_message(token, channel, content):
    url = f"https://discord.com:443/api/v9/channels/{channel}/messages"
    headers = {"Authorization": f"{token}", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36", "Content-Type": "application/json"}
    json={"content": f"{content}"}
    a = requests.post(url, headers=headers, json=json)
    print(a.status_code)
    print(content)

while 1:
    post_message(choice(config["token"]),choice(config['channels']),"@everyone " + choice(content_list))