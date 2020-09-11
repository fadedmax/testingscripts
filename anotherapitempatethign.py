import requests
import json
import time
import os
import sys



response = requests.get("https://api.mcsrvstat.us/1/play.quantumfactions.tk:19132")
if response.status_code == 200:
    print("api 1 worked")

response = requests.get("https://mcapi.us/server/status?ip=play.nethergames.org&port=")
if response.status_code == 200:
    print("api 2 worked")

response = requests.get("https://api.minetools.eu/uuid/gamerboy79")
if response.status_code == 200:
    print("api 2 worked")
    json_response = response.json()
    dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
    debug = json_response
    print(json.dumps(debug, indent=4))
    










