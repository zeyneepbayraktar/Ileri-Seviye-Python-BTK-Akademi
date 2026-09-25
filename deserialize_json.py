import json

with open("product.json") as file:
    data = json.load(file)

print(data)
print(type(data))
print(data["title"])

# serialize => encode
# deserialize => decode