data = [
    {
        "id": 1,
        "title": "Macbook Pro",
        "price": 90000,
    },
    {
        "id": 1,
        "title": "Macbook Pro",
        "price": 70000,
    }
]

import json

product = {
        "id": 3,
        "title": "Phone",
        "price": 40000,
    }
with open("products.json") as file:
    products = json.load(file)

products.append(product)

with open("products.json", "w", encoding = "utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)



