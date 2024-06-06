import json

# with open("product.json") as file:
#     data = json.load(file)

# json string
data = """
    {
        "id":1,
        "title":"Macbook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["Red","Blue"]
    }
"""

data = json.loads(data)

print(data)
print(type(data))
print(data["title"])
print(data["price"])
print(data["colors"])

# serialize => encode
# deserialize => decode

