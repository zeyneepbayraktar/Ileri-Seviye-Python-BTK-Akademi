# ============================================================
# SUM VE ROUND FONKSIYONLARI
# sum(iterable)     -> elemanlarin toplamini doner
# round(sayi, n)     -> sayiyi virgulden sonra n basamaga yuvarlar
# ============================================================

products = [
    {"title": "iphone 15", "price": 60000},
    {"title": "iphone 14", "price": 40000},
    {"title": "iphone 13", "price": 35000},
    {"title": "iphone 12", "price": 0},
]

# --- 1) sum ile toplam fiyat ---
sonuc = sum(urun["price"] for urun in products)
print("1) toplam fiyat:", sonuc)  # 135000

# --- 2) Butun urunlerin ortalamasi (fiyati 0 olan da dahil) ---
ort = (sum(urun["price"] for urun in products)) / (len(products))
print("2) tum urunlerin ortalamasi:", ort)  # 33750.0

# --- 3) Fiyati 0 olanlari dahil etmeden ortalama ---
urunAdeti = len([urun for urun in products if urun["price"] > 0])
ort2 = (sum(urun["price"] for urun in products)) / urunAdeti  # 0'lari dahil etmeden ortalama
print("3) 0'lar haric ortalama:", ort2)  # 45000.0

# --- 4) round ile ortalamalari okunabilir hale getirme ---
print("4a) ort (2 basamak):", round(ort, 2))
print("4b) ort2 (2 basamak):", round(ort2, 2))
