import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos", params= {
    "userId": "1",
    "completed": "true"
})

todos = response.json()

sonuc = todos

# print(sonuc[0]["title"])
print(sonuc)