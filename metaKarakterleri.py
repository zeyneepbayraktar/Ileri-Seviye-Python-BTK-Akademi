#META KARAKTERLER#

# import re

# text = "123 BTK Akademi Ileri Seviye Python BTK 456 x 789"
# pattern = r"\d\d\d"

# match = re.search(pattern, text)
# print(match)

# match = re.findall(pattern, text)
# sonuc = match
# print(sonuc)

# match = re.finditer(pattern , text)

# for i in match:
#     print(i.group())

# # # #

import re

text = "1 23 456 7890 BTK Akademi Ileri Seviye Python BTK 456 x 789"
# pattern = r"\d+"
# pattern = r"\d{2,3}"
pattern = r"\d{3,}"
# pattern = r"\d{,5}"

match = re.findall(pattern, text)
sonuc = match
print(sonuc)


