# ============================================================
# ÖZEL ITERATOR SINIFI
# Python'un iterator protokolünü kendi sınıfımızla uyguluyoruz.
# __iter__() ile nesneyi iterable hale getirir, __next__() ile
# sıradaki değeri üretiriz. StopIteration hatası ile döngüyü sonlandırırız.
# ============================================================

class Mynumber:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

iterator = iter(Mynumber(20,30))
# print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
