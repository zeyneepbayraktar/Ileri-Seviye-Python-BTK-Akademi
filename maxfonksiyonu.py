# ============================================================
# MAX VE MIN FONKSIYONLARI
# max()/min() bir iterable icindeki en buyuk/en kucuk degeri bulur.
# key parametresi ile "buyuk/kucuk" karsilastirmasinin neye gore
# yapilacagini belirleyebiliriz.
# ============================================================

# --- 1) Sayilarda dogrudan kullanim ---
sayilar = [1, 2, 3, 4, 5]
sonuc = max(sayilar)
print("1a) max:", sonuc)  # 5
sonuc = min(sayilar)
print("1b) min:", sonuc)  # 1

# --- 2) key parametresi ile: en kisa/en uzun ismi bulma ---
isimler = ["ahmet", "ali", "zeynep"]

# key = lambda isim: len(isim)  -> her elemani karsilastirirken
# kendisi yerine len(isim) degerini kullan
sonuc = min(isimler, key=lambda isim: len(isim))
print("2a) en kisa isim (key ile):", sonuc)  # 'ali'

sonuc = max(isimler, key=lambda isim: len(isim))
print("2b) en uzun isim (key ile):", sonuc)  # 'zeynep'

print("-----")

# --- 3) Ayni sonucu generator expression ile alma ---
# Burada elemanin kendisi degil, uzunluklarin min/max'i donuyor (isim degil, sayi).
sonuc = min(len(isim) for isim in isimler)
print("3a) en kisa ismin uzunlugu:", sonuc)  # 3

sonuc = max(len(isim) for isim in isimler)
print("3b) en uzun ismin uzunlugu:", sonuc)  # 6
