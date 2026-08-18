# ============================================================
# SPECIAL (DUNDER / MAGIC) METHODS
# Adi cift alt tire ile baslayip biten methodlardir: __init__, __repr__ ...
# Python'un yerlesik davranislarini kendi class'imiz icin tanimlariz;
# biz cagirmayiz, Python uygun anda otomatik cagirir.
#   __init__ -> Movie(...)  yazinca
#   __repr__ -> print(m) / repr(m) yazinca
#   __len__  -> len(m)      yazinca
# ============================================================

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration
    # Nesnenin metin gosterimi. Tanimlamazsak
    # <__main__.Movie object at 0x...> gibi okunmaz bir cikti alirdik.
    def __repr__(self):
        return f"{self.title}, {self.director}, {self.year}, {self.duration}"
    # len(nesne) cagrildiginda ne donecegini belirler. Tam sayi donmeli.
    def __len__(self):
        return self.duration

m = Movie("film adi","yonetmen", "yayin tarihi", 120)

# NOT: m.__repr__ (parantezsiz) methodun KENDISINI yazdirir.
# Metni gormek icin print(m), repr(m) ya da m.__repr__() yazilir.
print(m.__repr__)
print(len(m))  # 120
