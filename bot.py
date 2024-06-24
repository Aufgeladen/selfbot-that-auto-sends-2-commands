import requests
import json
import time
import random

# Replace with your channel ID and bot token
channel_id = '634477598222581782'
bot_token = '<hier dein discord token>'

url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
headers = {
    "Authorization": f"{bot_token}",
    "Content-Type": "application/json"
}

while True:
    # Generate a random nonce for work command
    nonce_work = str(random.randint(1000000000000000000, 9999999999999999999))  # 19-digit random number
    
    # Payload for ",work" command
    payload_work = {
        "content": ",work",
        "flags": 0,
        "nonce": nonce_work,
        "tts": False
    }
    
    # Send the work command
    response = requests.post(url, headers=headers, data=json.dumps(payload_work))
    print("Work Command - Status Code:", response.status_code)
    print("Work Command - Response:", response.json())
    
    # Wait for 4 seconds
    time.sleep(4)
    
    # Generate a random nonce for dep all command
    nonce_dep_all = str(random.randint(1000000000000000000, 9999999999999999999))  # 19-digit random number
    
    # Payload for ",dep all" command
    payload_dep_all = {
        "content": ",dep all",
        "flags": 0,
        "nonce": nonce_dep_all,
        "tts": False
    }
    
    # Send the dep all command
    response = requests.post(url, headers=headers, data=json.dumps(payload_dep_all))
    print("Dep All Command - Status Code:", response.status_code)
    print("Dep All Command - Response:", response.json())
    
    # hier custom zeit über 300
    time.sleep(312)
