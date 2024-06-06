import json

product = {
    "id":2,
    "title":"Macbook Pro",
    "price": 90000,
    "rating": "4.5",
    "category": "Bilgisayar",
    "colors": ["Red","Blue"]
}

print(product)
print(product["title"])
print(type(product))

# sonuc = json.dumps(product)

# print(sonuc)
# print(sonuc["title"])
# print(type(sonuc))

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, ensure_ascii=False, indent=2)