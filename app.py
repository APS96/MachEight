import requests
import json
from player_height import height_func

data=requests.get("https://mach-eight.uc.r.appspot.com/")
players=json.loads(data.text)['values']
print("Enter integer input: ")
input_height=input()
result = height_func(players,input_height)