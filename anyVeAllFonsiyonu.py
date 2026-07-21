# ============================================================
# ANY VE ALL FONKSIYONLARI
# all(iterable) -> TUM elemanlar True/truthy ise True doner
# any(iterable) -> EN AZ BIR eleman True/truthy ise True doner
# ============================================================

# --- 1) Temel dogruluk tablosu: hepsi True ---
sonuc = all([True, True, True])
print("1a) all(hepsi True):", sonuc)  # True

sonuc = any([True, True, True])
print("1b) any(hepsi True):", sonuc)  # True

# --- 2) Bir tanesi False olunca ---
sonuc = all([True, True, False])
print("2a) all(biri False):", sonuc)  # False

sonuc = any([True, True, False])
print("2b) any(biri False):", sonuc)  # True (en az biri True oldugu icin)

# --- 3) Hepsi False ---
sonuc = all([False, False, False])
print("3a) all(hepsi False):", sonuc)  # False

sonuc = any([False, False, False])
print("3b) any(hepsi False):", sonuc)  # False

# --- 4) Sayilarla: 0 falsy, diger sayilar truthy kabul edilir ---
sayilar = [1, 2, 3, 4, 5, 0, -1]
sonuc = all(bool(sayi) for sayi in sayilar)
print("4a) all(sayilar, 0 var):", sonuc)  # False (listede 0 oldugu icin)

sonuc = any(bool(sayi) for sayi in sayilar)
print("4b) any(sayilar, 0 var):", sonuc)  # True (0'dan farkli sayilar var)

# ============================================================
# UYGULAMA: Kullanici isimlerinin ilk harfini kontrol etme
# ============================================================

users = ["ahmet", "ali", "cinar"]

# --- 5) Hepsi 'a' ile mi basliyor? ---
sonuc = all(user[0] == "a" for user in users)
print("5) hepsi 'a' ile basliyor mu:", sonuc)  # False ("cinar" basliyor 'c' ile)

# --- 6) En az biri 'a' ile mi basliyor? ---
sonuc = any(user[0] == "a" for user in users)
print("6) en az biri 'a' ile basliyor mu:", sonuc)  # True ("ahmet", "ali")
