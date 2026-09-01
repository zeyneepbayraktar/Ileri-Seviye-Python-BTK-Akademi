import re

text = "BTK Akademi Ileri Seviye Python BTK"
pattern = "BTK"

match = re.search(pattern, text)
sonuc = match
print(sonuc)

sonuc = match.span()
print(sonuc)

match = re.findall(pattern, text)
sonuc = match
print(sonuc)
