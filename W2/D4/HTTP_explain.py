# HTTP - HYPERTEXT TRANSFER PROTOCOL
# IMPORTANT ASPECTS ABOUT HTTP
# - CONNECTIONLESS
# - CAN DELIVERY ANY SORT OF DATA
import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get("https://api.chucknorris.io/jokes/random")
# print(response.text) # BODY OF THE HTTP RESPONSE
# print(response.headers)
print(response.status_code)

#
# print(response.text)
# data = json.loads(response.text)
#
#
# with open(f"{dir_path}/jokes.json", "w", encoding="utf - 8") as f:
#     json.dump(data, f, indent=2, skipkeys= True)
#
# print(data["value"])

# REST API