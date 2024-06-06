data =   {
    "2": {
      "title": "Macbook Air",
      "price": 70000
    },
    "3": {
      "title": "Samsung S24",
      "price": 70000
    }
}

import json

with open("products.json") as file:
    products = json.load(file)

print(products["2"])
print(products["3"])

# products.update({
#     "1": {
#       "title": "Macbook Pro",
#       "price": 80000
#     }
# })

products.update({
    "3": {
      "title": "Samsung S25",
      "price": 90000
    }
})

products.pop("1")

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)