# ============================================================
# INSTANCE METHODS (ORNEK METHODLARI)
# Ilk parametresi self olan, yani nesnenin kendi verisi uzerinde
# calisan methodlardir.
# - Nesnenin verisini OKUYABILIR    (ornek: calculate_total)
# - Nesnenin verisini DEGISTIREBILIR (ornek: apply_discount)
# ============================================================

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price =price
        self.quantity = quantity
    # Nesnenin verisini okur, degistirmez: fiyat * adet
    def calculate_total(self):
        return self.price * self.quantity
    # Nesnenin verisini degistirir: fiyati indirim oranina gore gunceller
    # rate = 0.5 => %50 indirim => fiyat * (1 - 0.5)
    def apply_discount(self, rate):
        self.price = self.price * (1 - rate)

item1 = CartItem("Telefon", 30000, 5)
item2 = CartItem("Bilgisayar", 25000, 3)

# --- Indirim oncesi fiyatlar ---
print(item1.price)  # 30000
print(item2.price)  # 25000

# --- Method cagirma: item1.calculate_total() -> self = item1 ---
print(item1.calculate_total())  # 30000 * 5 = 150000
print(item2.calculate_total())  # 25000 * 3 = 75000

# --- Nesnenin verisini degistiren method ---
item1.apply_discount(0.5)
item2.apply_discount(0.5)
print(item1.price)  # 15000.0
print(item2.price)  # 12500.0
