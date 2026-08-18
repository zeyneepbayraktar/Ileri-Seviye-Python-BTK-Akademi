# ============================================================
# PROPERTIES (@property)
# Bir attribute'a dogrudan erisimi kapatip, okuma/yazma islemlerini
# method uzerinden kontrol etmemizi saglar (encapsulation).
#   _price        -> "disaridan dokunma" anlaminda tek alt tire ile yazilan
#                    gercek veri (private convention)
#   @property     -> getter: p.price yazinca calisir
#   @price.setter -> setter: p.price = 100 yazinca calisir
# Boylece kullanici normal attribute gibi yazar ama araya
# dogrulama (validation) kurali koyabiliriz.
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("negatif deger alamaz")

    # --- GETTER: degeri okurken calisir ---
    @property
    def price(self):
        return self._price
    # --- SETTER: degeri atarken calisir, kural burada ---
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("negatif deger alamaz")

# Okuma: aslinda price() methodu calisir, parantez yazmayiz
p = Product("Telefon", 80000)
print(p.price)  # 80000
# Yazma: setter calisir ve deger kontrol edilir
p.price = 90000
print(p.price)  # 90000
