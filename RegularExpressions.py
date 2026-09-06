# ============================================================
# REGULAR EXPRESSIONS (REGEX)
# Metin içinde belirli desenleri aramak, eşleştirmek ve bulmak
# için re (regular expressions) modülü kullanılır.
# ============================================================

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
