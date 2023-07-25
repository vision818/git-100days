import requests, json

result = requests.get("https://randomuser.me/api/")

user = result.json()

# print(json.dumps(user, indent = 2))

name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}"""

print(name)