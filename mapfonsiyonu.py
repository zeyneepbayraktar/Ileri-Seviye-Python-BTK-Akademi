# ============================================================
# MAP VE FILTER FONKSIYONLARI
# map(fonksiyon, iterable)    -> her elemana fonksiyonu uygular
# filter(fonksiyon, iterable) -> fonksiyon True donduren elemanlari birakir
# İkisi de bir "map/filter object" dondurur, bu yuzden genelde list() ile sarmalariz.
# ============================================================

# --- 1) map + normal fonksiyon ---
sayilar = [1, 2, 3, 4, 5]

def kareAl(sayi):
    return sayi ** 2

sonuc = list(map(kareAl, sayilar))
print("1) map + fonksiyon:", sonuc)  # [1, 4, 9, 16, 25]

# --- 2) map + lambda (ayni islem, daha kisa) ---
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
print("2) map + lambda:", sonuc)  # [1, 4, 9, 16, 25]

# --- 3) map ile tip donusumu: string listesini int listesine cevirme ---
sayilar_str = ["1", "2", "3"]
sonuc = list(map(int, sayilar_str))
print("3) map ile str -> int:", sonuc)  # [1, 2, 3]

# --- 4) map ile dict listesinden tek bir alani cekme ---
kullanicilar = [
    {"ad": "Ahmet", "soyad": "Yilmaz"},
    {"ad": "Ali", "soyad": "Cengiz"},
]
sonuc = list(map(lambda kisi: kisi["ad"], kullanicilar))
print("4) map ile dict'ten alan secme:", sonuc)  # ['Ahmet', 'Ali']

# --- 5) filter ile kosula uymayanlari eleme ---
sayilar2 = [1, 2, 0, -1, -3]
sonuc = list(filter(lambda x: x < 0, sayilar2))
print("5) filter ile negatifler:", sonuc)  # [-1, -3]

# --- 6) map + filter'i zincirleme kullanma ---
isimler = ["Cinar", "Ali", "ada"]

# once hepsini buyuk harfe cevir
buyuk_isimler = list(map(lambda x: x.upper(), isimler))
print("6a) buyuk harfe cevrilmis:", buyuk_isimler)  # ['CINAR', 'ALI', 'ADA']

# sonra sadece "A" ile baslayanlari filtrele (map'in ciktisini filter'a veriyoruz)
a_ile_baslayanlar = list(
    filter(lambda x: x[0] == "A", map(lambda x: x.upper(), isimler))
)
print("6b) buyutup A ile filtrelenmis:", a_ile_baslayanlar)  # ['ALI', 'ADA']
