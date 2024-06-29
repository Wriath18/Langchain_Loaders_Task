import requests

url = "http://127.0.0.1:5000/search"
query = {"query": "Free Demo"}

response = requests.post(url, json=query)
print(response.json())
