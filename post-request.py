import requests
import json

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
    "userId": 1,
    "title": "yeni gonderi",
    "body": "yeni gonderi aciklamasi"
  })

sonuc = response
print(sonuc) #<Response [201]> Created


sonuc = response.text
print(sonuc)

sonuc = response.json()
print(sonuc)

sonuc = response.headers
print(sonuc)

