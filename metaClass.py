# ============================================================
# METACLASS ÖRNEKLERI
# Metaclass, sınıfların kendisini üreten "sınıfın sınıfıdır".
# Burada __new__ metodu override edilerek class attribute'larin
# isimleri büyütülür ve istenmeyen alanlar filtrelenir.
# ============================================================

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)
    

class Person(metaclass = Meta):
    x=5
    y=10
    _age = 10
    def hello(self):
        print("merhaba")

p = Person()

sonuc = p.X
sonuc = p.Y 
sonuc = p._age

print(sonuc)