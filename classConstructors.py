# ============================================================
# CLASS VE CONSTRUCTOR (__init__)
# class => sinif. Ortak ozellikleri ve davranislari olan
# nesneler icin bir "sablon"dur.
# __init__ => yapici method (constructor). Nesne olusturulurken
# Python tarafindan otomatik olarak cagrilir ve nesnenin
# baslangic ozelliklerini (attribute) belirler.
# ============================================================

# class => sinif
class CartItem:
    # constructor => yapici method
    # self => uzerinde calisilan nesnenin kendisi.
    # Her methodun ilk parametresi olarak yazilir, cagirirken verilmez.
    def __init__(self, name, price, quantity):
        # self.xxx = ... satirlarinin her biri nesneye ait
        # bir "instance attribute" olusturur.
        self.name = name
        self.price =price
        self.quantity = quantity
        

# Nesne (instance) olusturma: CartItem(...) yazdigimiz anda __init__ calisir.
item1 = CartItem("Telefon", 30000, 5)
item2 = CartItem("Bilgisayar", 25000, 3)
