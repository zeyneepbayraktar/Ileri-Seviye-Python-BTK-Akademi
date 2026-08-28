# ============================================================
# ILERI DUZEY FONKSIYONLAR
# Bu dosya iç içe fonksiyonlar, fonksiyondan fonksiyon döndürme ve
# fonksiyonları parametre olarak geçme gibi ileri düzey konuların
# örnek çalışma notlarını içerir.
# ============================================================

# Ic ice fonksiyon

# def outer(number):
#     def inner(number):
#         print(number)

#     inner(number)

# outer(10)

# def factorial(sayi):
#     if not isinstance(sayi, int):
#         raise TypeError("number must be an int")

#     if not sayi >= 0:
#         raise ValueError("must be zero or positive")
#     def innerfactorial(sayi):
#         if sayi <= 0:
#             return 1

#         return sayi * innerfactorial(sayi - 1)
    
#     return innerfactorial(sayi)

# sonuc = factorial(3)
# print(sonuc)

# try:
#     sonuc = factorial("4")
#     print(sonuc)
# except Exception as ex:
#     print(ex)

# sonuc = factorial(3)
# print(sonuc)

#fonksiyondan geriye fonksiyon dondurme

# def usAlma(taban):
#     def inner(us):
#         return taban ** us
#     return inner
# sonuc = usAlma(2)(3)
# print(sonuc)

# def yetkiSorgulama(sayfa):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolu {sayfa} sayfasindan ulasilabilir"
#         else:
#             return f"{role} rolu {sayfa} sayfasina ulasamaz"
#     return inner
# yetki = yetkiSorgulama("urun guncelleme")
# sonuc = yetki("User")
# print(sonuc)

# def islem(islemadi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
#     def carpim(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim
#     if islemadi == "Toplama":
#         return toplam
#     if islemadi == "Carpma":
#         return carpim

# toplama = islem("Toplama")
# carpim = islem("Carpma")

# sonuc = toplama(12, 20)
# sonuc1 = carpim(10, 32)

# print(sonuc)
# print(sonuc1)

# fonksiyonlari parametre olarak gonderme

# def filter(fn, liste):
#     result =[]
#     for item in liste:
#         if fn(item):
#             result.append(item)
#     return result

# def isEven(num):
#     return num%2 == 0
# def isPositive(num):
#     return num > 0

# sayilar = [1, 2, 3, 57, 29, 13, 828, 12, 80, 0, -3]

# sonuc = filter(isEven, sayilar)
# print(sonuc)
# sonuc = filter(isPositive, sayilar)
# print(sonuc)



