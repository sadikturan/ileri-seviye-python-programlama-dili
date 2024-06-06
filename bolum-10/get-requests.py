import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

sonuc = response
sonuc = type(response)
sonuc = response.status_code
sonuc = response.headers
sonuc = response.headers["Content-Type"]
sonuc = response.url
sonuc = response.encoding
sonuc = response.text
sonuc = type(response.text)
posts = json.loads(response.text)
sonuc = posts[0]["title"]

for item in posts:
    if item["userId"] == 1:
        print(item["title"])

# print(sonuc)