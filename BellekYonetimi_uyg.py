# ============================================================
# BELLEK YÖNETİMİ VE GENERATOR UYGULAMALARI
# Bu dosya generator örnekleri, Fibonacci dizisi ve bellek verimliliği karşılaştırmasını gösterir.
# Bu açıklama sadece dosyanın amacını anlatmak içindir.
# Kod mantığı değiştirilmeden, örneklerin okunabilirliği artırılmıştır.
# ============================================================

# (1-sonsuz arasi her sayinin  karesini getiren fonk)
def SayiUret():
    sayi = 0
    while True:
        yield sayi**2
        sayi += 1

generator = SayiUret()

# print(next(generator))
# for i in generator:
#     print(i)

#fibonacci serisini hem normal hem de generator ile olusturun
def fibo_list(max):
    sayilar = []

    a, b = 0, 1

    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a+b

    return sayilar

# print(fibo_list(900))

def fibo_generator(max):
    a, b = 0, 1
    count = 0

    while count <= max:
        a, b = b, a+b
        yield b
        count += 1

# for i in fibo_generator(90):
#     print(i)

#performans degerlendirmesi
import sys

liste = [i for i in range(900)]
print(sys.getsizeof(liste))

genarator = (i for i in range(900))
print(sys.getsizeof(generator))

import time

list_start_time = time.time()
sum = [i for i in range(900)]
list_stop= time.time() - list_start_time

generator_start_time = time.time()
sum = [i for i in range(900)]
generator_stop= time.time() - generator_start_time

print(list_stop)
print(generator_stop)