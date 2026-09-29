db = {
    "users": {
        "sadikturan":{
            "firstname": "Sadik",
            "lastname": "Turan"
        },
        "cinarturan":{
            "firstname": "Cinar",
            "lastname": "Turan"
        }
    },
    "products":{
        "1":{
                "title": "Macbook Pro",
                "price": 80000
            },
        "2": {
            "title": "Macbook Air",
            "price": 70000
            },
        "3": {
            "title": "Samsung",
            "price": 70000
            }
    }
}

import json

# with open("db.json", "w", encoding = "utf-8") as file:
#     json.dump(db, file, ensure_ascii=False, indent=2)

with open("db.json") as file:
    data = json.load(file)

print(data["users"])
print(data["products"]["2"])

data["products"].update({
        "3": {
            "title": "Samsung S26",
            "price": 90000
        }})

with open("db.json", "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

