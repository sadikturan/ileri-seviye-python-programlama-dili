import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
    "userId": 1,
    "title": "yeni gönderi",
    "body": "yeni gönderi açıklaması"
})

sonuc = response
sonuc = response.text
sonuc = response.json()
sonuc = response.headers

print(sonuc)
