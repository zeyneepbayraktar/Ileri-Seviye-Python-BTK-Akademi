# ============================================================
# GENERATOR KAVRAMI
# Generator, bir fonksiyonun yield anahtar kelimesi ile değer üretmesine
# olanak tanır. Bellek açısından daha verimli çalışır; tüm değerleri tek
# seferde saklamak yerine ihtiyaç anında üretir.
# ============================================================

def counter(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi +=1

generator = counter(20)
# for i in generator:
#     print(i)

sonuc = list(generator)
print(sonuc)