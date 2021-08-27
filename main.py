import requests 
import json

token = "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"

#https://github.com/santiagousach/codea-it/blob/master/api.json
url = 'https://raw.githubusercontent.com/santiagousach/codea-it/master/api.json'


r = requests.get(url)

apis = r.json()


for i in apis[]:
    print(i)