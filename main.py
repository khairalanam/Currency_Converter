import requests
import json

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)
