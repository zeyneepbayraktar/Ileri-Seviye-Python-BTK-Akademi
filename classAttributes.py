# ============================================================
# CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE
# - Class attribute : class govdesinde tanimlanir, TUM nesneler
#   icin ORTAKTIR. (ornek: discount_rate, item_count)
# - Instance attribute: __init__ icinde self.xxx ile tanimlanir,
#   HER NESNEYE OZELDIR. (ornek: name, price, quantity)
# ============================================================

class CartItem:
    # --- class attribute'lar: tum urunler icin ortak ---
    discount_rate = 0.8   # %20 indirim (fiyatin %80'i kalir)
    item_count = 0        # kac tane CartItem uretildigini sayar
    def __init__(self, name, price, quantity):
        # --- instance attribute'lar: her urune ozel ---
        self.name = name
        self.price =price
        self.quantity = quantity
        # Sayaci class uzerinden artiriyoruz ki tum nesnelerde ayni deger olsun.
        # self.item_count += 1 yazsaydik nesneye ozel yeni bir attribute olusurdu.
        CartItem.item_count += 1
    def calculate_total(self):
        return self.price * self.quantity
    def apply_discount(self):
        # Indirim orani nesneden degil, class'tan okunur.
        self.price = self.price * CartItem.discount_rate

item1 = CartItem("Telefon", 30000, 5)
item2 = CartItem("Bilgisayar", 25000, 3)

# --- Instance attribute'lar nesneye ozeldir ---
print(item1.price)  # 30000
print(item2.price)  # 25000
print("-------")
# --- Toplam hesaplama ---
print(item1.calculate_total())  # 150000
print(item2.calculate_total())  # 75000
print(item1.price)
print(item2.price)
print("-------")
# --- __dict__ sadece INSTANCE attribute'lari gosterir ---
# discount_rate ve item_count burada YOKTUR, cunku onlar class'a aittir.
print(item1.__dict__)
print("-------")
# --- Ortak indirim oranini uygulama ---
item1.apply_discount()
print(item1.calculate_total())  # 30000*0.8*5 = 120000.0
item2.apply_discount()
print(item2.calculate_total())  # 25000*0.8*3 = 60000.0
print("-------")
# --- Sayac: class attribute paylasildigi icin kac nesne uretildigini tutar ---
print(CartItem.item_count)  # 2

