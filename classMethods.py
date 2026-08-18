# ============================================================
# CLASS METHODS (@classmethod)
# Ilk parametresi cls olan, yani nesneye degil CLASS'IN KENDISINE
# bagli calisan methodlardir. Nesne olusturmadan cagrilabilir.
# Iki tipik kullanim:
#   1) Class attribute'lar uzerinde islem yapmak (ornek: item_count)
#   2) Alternatif constructor yazmak (ornek: create_item)
# ============================================================

class CartItem:
    discount_rate = 0.8
    item_count = 0

    # --- Class attribute okuyan class method ---
    # cls = CartItem class'inin kendisi
    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane urun olusturuldu."
    # --- Alternatif constructor ---
    # "Telefon,30000,5" gibi bir metinden nesne uretir.
    # cls(...) yazmak CartItem(...) yazmakla aynidir; ama kalitimda
    # alt class'tan cagrilirsa alt class'tan nesne uretir.
    # NOT: split() her zaman STRING doner (ve bosluklar da gelir),
    # yani buradaki price/quantity sayi degil metindir.
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls (name, price, quantity)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price =price
        self.quantity = quantity
        CartItem.item_count += 1
    def calculate_total(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

# --- Class method nesne olmadan da cagrilabilir ---
print(CartItem.display_item_count())  # 0 tane urun olusturuldu.

# --- Normal yoldan nesne uretme ---
item1 = CartItem("Telefon", 30000, 5)
item2 = CartItem("Bilgisayar", 25000, 3)

# --- Alternatif constructor ile metinden nesne uretme ---
CartItem.create_item("mouse, 150, 2")

# create_item icinde de __init__ calistigi icin sayac yine artar.
print(CartItem.display_item_count())  # 3 tane urun olusturuldu.

