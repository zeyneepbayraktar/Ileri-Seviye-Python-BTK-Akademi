# ============================================================
# LIST COMPREHENSION - UYGULAMA SORULARI
# Her soru: (a) problem tanımı, (b) çözüm olarak yorum halinde
# ============================================================

# --- 1) 1 ile 100 arasindaki sayilardan 12'ye tam bolunebilenlerin
#         listesini olusturunuz. ---
liste1 = [sayi for sayi in range(1, 101) if sayi % 12 == 0]
print("1) 12'ye bolunenler:", liste1)

# --- 2) Verilen text icindeki rakamlari iceren bir liste olusturunuz.
#         text = "Hello 12345 World" => ['1','2','3','4','5'] ---
text = "Hello 12345 World"
liste2 = [i for i in text if i.isdigit()]
print("2) metindeki rakamlar:", liste2)

# --- 3) Sicakliklar listesindeki her hava sicaklik bilgisine gore
#         4 derecenin altinda "Buzlanma Tehlikesi" yaziniz.
#         sicakliklar = [20, 15, 4, 0, -5, -2]
#         => [20, 15, 4, 'Buzlanma Tehlikesi', 'Buzlanma Tehlikesi', 'Buzlanma Tehlikesi'] ---
sicakliklar = [20, 15, 4, 0, -5, -2]
liste3 = [i if i >= 4 else "Buzlanma Tehlikesi" for i in sicakliklar]
print("3) sicaklik durumu:", liste3)

# --- 4) ogrenciler ve notlar listesinde notu 50'den fazla olan ogrencileri
#         ekrana dict verisinde yazdiriniz.
#         ogrenciler = ["Ali", "Canan", "Ahmet"], notlar = [50, 60, 80]
#         => {'Canan': 60, 'Ahmet': 80}
#         ipucu: new_dict = {key_expression: value_expression for item in iterable} ---
ogrenciler = ["Ali", "Ahmet", "Canan"]
notlar = [50, 60, 80]

# once (isim, not) ciftlerinden olusan bir liste kuruyoruz
ogrenci_not_ciftleri = [(ogrenciler[i], notlar[i]) for i in range(len(ogrenciler))]
print("4a) isim-not ciftleri:", ogrenci_not_ciftleri)

# sonra bu ciftlerden, notu 50'den buyuk olanlari dict comprehension ile filtreliyoruz
basarili_ogrenciler = {k: v for (k, v) in ogrenci_not_ciftleri if v > 50}
print("4b) 50'den basarili ogrenciler:", basarili_ogrenciler)

# --- 5) Asagida for dongusu ile yazilan uygulamayi list comprehension ile yaziniz. ---
ikili_kombinasyonlar_for = []
for x in range(3):
    for y in range(3):
        ikili_kombinasyonlar_for.append((x, y))
print("5a) for dongusu ile:", ikili_kombinasyonlar_for)

# ic ice for dongusu, list comprehension icinde soldan saga ayni sirayla yazilir
ikili_kombinasyonlar_lc = [(x, y) for x in range(3) for y in range(3)]
print("5b) list comprehension ile:", ikili_kombinasyonlar_lc)
