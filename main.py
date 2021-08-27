import requests as r
import json

f = open('api.json')

data = json.load(f)


x = r.text('api.json')

print(x)