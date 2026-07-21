# ============================================================
# LIST COMPREHENSION
# Bir listeyi tek satırda, döngü yazmadan oluşturmamızı sağlayan
# Python'a özgü kısa sözdizimi.
# Genel kalıp: [ifade for eleman in iterable]
# ============================================================

# --- 1) Klasik for döngüsü ile liste oluşturma ---
sayilar = []
for i in range(5):
    sayilar.append(i)
print("for dongusu ile:", sayilar)  # [0, 1, 2, 3, 4]

# --- 2) Aynı işlemin list comprehension hali ---
# "range(5) içindeki her sayi için, sayi'yi listeye ekle" gibi okunur.
sayilar2 = [sayi for sayi in range(5)]
print("list comprehension ile:", sayilar2)  # [0, 1, 2, 3, 4]

# --- 3) String de iterable olduğu için karakterler üzerinde de çalışır ---
isim = "zeynep"

for i in isim:
    print("harf:", i)

isim2 = [i for i in isim]
print("stringden liste:", isim2)  # ['z', 'e', 'y', 'n', 'e', 'p']

# ============================================================
# KOSULLU LIST COMPREHENSION
# ============================================================

sayilar3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- 4) if ile FİLTRELEME ---
# Sadece koşulu sağlayan elemanlar listeye girer, diğerleri elenir.
# Kalıp: [ifade for eleman in iterable if kosul]
ciftler = [sayi for sayi in sayilar3 if sayi % 2 == 0]
print("sadece ciftler:", ciftler)  # [2, 4, 6, 8]

# --- 5) if/else ile DEĞER DÖNÜŞTÜRME (filtreleme değil!) ---
# Burada eleman elenmez, koşula göre başka bir değere dönüştürülür.
# Kalıp: [ifade1 if kosul else ifade2 for eleman in iterable]
tek_cift = [sayi if sayi % 2 == 0 else "tek sayi" for sayi in sayilar3]
print("cift/tek etiketli:", tek_cift)
# ['tek sayi', 2, 'tek sayi', 4, 'tek sayi', 6, 'tek sayi', 8, 'tek sayi']

# ============================================================
# UYGULAMA: Fiyat listesine KDV ekleme
# ============================================================

urun_fiyat = [3000, 1000, 4000, 0, 5000]

# --- 6) if ile filtreleme: fiyati 0 olan urunu tamamen listeden cikarir ---
vergili_filtreli = [fiyat * 1.20 for fiyat in urun_fiyat if fiyat > 0]
print("KDV'li (0'lar elenmis):", vergili_filtreli)

# --- 7) if/else ile donusturme: fiyati 0 olan urun listede kalir,
#         ama sayi yerine aciklayici bir metin yazilir ---
vergili_donusturulmus = [
    fiyat * 1.20 if fiyat > 0 else "hesaplanamadi" for fiyat in urun_fiyat
]
print("KDV'li (0'lar etiketli):", vergili_donusturulmus)
