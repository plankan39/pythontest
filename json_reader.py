import json
import requests

requests.request()

file_name = 'user.json'

users = {}
with open(file_name) as f:
    users = json.load(f)
    print(f"userName: {users['userName']} pw: {users['password']}")
users['password'] = 'hahahackad'

with open(file_name, 'w') as f:
    json.dump(users, f, indent=2)


with open(file_name) as f:
    users = json.load(f)
    print(f"userName: {users['userName']} pw: {users['password']}")
