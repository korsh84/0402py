#!F:\Docs\2021_devops\pythonProject\venv\Scripts\python.exe

import requests
#import os
import json
from pprint import pprint

token = "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"
headers = {
  #  "Authorization": "token {}".format(token),
   # "Content-Type": "application/json",
    "Accept": "application/vnd.github.v3+json"
}
username = "korsh84"
reponame = "0402py"
data = {
    "title": "Pull req via API",
    "body": "commit message test",
    head: test,
    base: main
}

#token = os.getenv('GITHUB_TOKEN', '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')
pull_url = "https://api.github.com/repos/{}/{}/pulls".format(username, reponame)
r = requests.get(pull_url, headers=headers, params=data)
r = requests.post(pull_url,  headers=headers, data=json.dumps(data))

#pprint(r.json())
