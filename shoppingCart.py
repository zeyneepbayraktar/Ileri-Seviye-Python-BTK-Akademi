# ============================================================
# UYGULAMA: ALISVERIS SEPETI
# Bu dosya simdiye kadarki OOP konularini tek ornekte birlestirir:
# class, constructor, instance method, class attribute, class method
# ve bir class'in baska bir class'in nesnelerini tutmasi.
#
# Uc class var:
#   CartItem     -> sepetteki tek bir urun
#   Coupon       -> indirim kuponu
#   ShoppingCart -> CartItem nesnelerini tutan sepet
# ============================================================

class CartItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane urun olusturuldu."
    @classmethod
    def create_item(cls, data_str):
        # "mouse, 150, 2" gibi bir metinden urun uretir
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

class Coupon:
    def __init__(self, code, discount):
        self.code = code          # kupon kodu
        self.discount = discount  # fiyatin kacta kaci odenecek (0.6 => %40 indirim)

c1= Coupon("code1", 0.6)
c2= Coupon("code2", 0.5)
c3= Coupon("code3", 0.9)


item1 = CartItem("Telefon", 30000, 5)
item2 = CartItem("Bilgisayar", 25000, 3)
item3 = CartItem("Bilgisayar 2", 26000, 6)
CartItem.create_item("mouse, 150, 2")

class ShoppingCart:
    # Tum sepetlerin ortak kullandigi kupon listesi (class attribute)
    coupon_list = [c1, c2, c3]

    def __init__(self,liste):
        self.liste = liste  # sepetteki CartItem nesneleri

    # --- Sepet islemleri (instance methodlar) ---
    def add_item(self,item):
        return self.liste.append(item)
    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
    def calculate_totals(self):
        # Her urunun kendi toplamini hesaplayip hepsini topluyoruz.
        # (list comprehension + sum konularinin OOP'deki kullanimi)
        return sum([item.calculate_total() for item in self.liste])
    def remove_item(self, CartItem):
        # Silinecek urun disindaki elemanlardan yeni bir liste kuruyoruz.
        self.liste = [item for item in self.liste if item != CartItem]
    def clear(self):
        self.liste = []

    # --- Kupon islemleri (class methodlar: kuponlar sepete degil class'a ait) ---
    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]

    @classmethod
    def get_coupon(cls, code):
        # filter ile kodu eslesen kuponlari suzup next ile ilkini aliyoruz
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))

    def apply_coupon(self, code):
        # Once kodun gecerli olup olmadigini kontrol et
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"gecersiz kod: {code}")

        coupon = ShoppingCart.get_coupon(code)

        # Sepetteki her urunun fiyatini kupon oraniyla guncelle
        for index in range(0, len(self.liste)):
            self.liste[index].price = self.liste[index].price * coupon.discount



# --- Sepeti kur ve urun ekle ---
sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_items()
print(sc.calculate_totals())  # 150000 + 75000 + 156000 = 381000

# --- Urun cikarma ---
sc.remove_item(item2)
sc.display_items()
# sc.clear()
sc.display_items()


# --- Kupon uygulama: %50 indirim ---
sc.apply_coupon(c2.code)
print(sc.calculate_totals())  # 153000.0
