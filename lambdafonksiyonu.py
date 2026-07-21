# ============================================================
# LAMBDA FONKSIYONLARI
# İsimsiz (anonymous), tek satırlık kısa fonksiyonlar.
# Kalıp: lambda parametreler: ifade  (ifade otomatik olarak return edilir)
# ============================================================

# --- 1) En basit hali: tanimlandigi anda cagirma (IIFE gibi) ---
sonuc = (lambda a: a ** 2)(3)
print("1) anlik cagrilan lambda:", sonuc)  # 9

# --- 2) Lambda'yi bir degiskene atayip normal fonksiyon gibi kullanma ---
kareAl = lambda a: a ** 2
print("2) degiskene atanmis lambda:", kareAl(3))  # 9

# --- 3) Birden fazla parametre alabilir ---
toplama = lambda a, b, c: a + b + c
print("3) coklu parametreli lambda:", toplama(1, 2, 3))  # 6

# --- 4) Lambda dondururek "closure" olusturma ---
# myFunc, n degerini "hatirlayan" bir lambda dondurur.
def myFunc(n):
    return lambda a: a * n

sonuc = myFunc(2)(3)
print("4) closure - tek seferlik cagri:", sonuc)  # 6


# --- 5) Closure'i tekrar kullanilabilir carpanlar uretmek icin kullanma ---
def myFunc2(n):
    return lambda a: a * n

carpma2 = myFunc2(2)  # her zaman 2 ile carpan bir fonksiyon
carpma3 = myFunc2(3)  # her zaman 3 ile carpan bir fonksiyon

print("5a) carpma2(3):", carpma2(3))  # 6
print("5b) carpma3(5):", carpma3(5))  # 15
