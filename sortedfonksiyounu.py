# ============================================================
# SORTED FONKSIYONU
# sorted(iterable) orijinal listeyi degistirmez, SIRALANMIS YENI bir
# liste dondurur. (list.sort() ise listeyi yerinde degistirir.)
# ============================================================

sayilar = [1, 6, 13, 2, 3, 56, 72, 198]

# --- 1) Varsayilan siralama: kucukten buyuge ---
sonuc = sorted(sayilar)  # kucukten buyuge
print("1) kucukten buyuge:", sonuc)  # [1, 2, 3, 6, 13, 56, 72, 198]

# --- 2) reverse=True ile: buyukten kucuge ---
sonuc = sorted(sayilar, reverse=True)  # buyukten kucuge
print("2) buyukten kucuge:", sonuc)  # [198, 72, 56, 13, 6, 3, 2, 1]

# not: max/min ornegindeki gibi sorted() de key=lambda ile
# ozel bir siralama kriteri alabilir, ör: sorted(isimler, key=lambda i: len(i))
