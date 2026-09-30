import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# sonuc = response
# print(sonuc)

# sonuc = type(response)
# print(sonuc)

# sonuc = response.status_code
# print(sonuc)

# sonuc = response.headers
# print(sonuc)

# sonuc = response.url
# print(sonuc)

# sonuc = response.encoding
# print(sonuc)

# sonuc = response.text 
# print(sonuc)

# sonuc = type(response.text)
# print(sonuc)

posts = json.loads(response.text)
sonuc = posts[0]["title"]
print(sonuc)

for item in posts:
    if item["userId"] == 1:
        print(item["title"])