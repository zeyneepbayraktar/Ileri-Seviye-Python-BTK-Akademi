# ============================================================
# GÜNLÜK SORU CHALLENGE
# Bu dosya her gün çözülmesi planlanan Python sorularının kısa örnek
# çözümlerini içerir. Konu listesi, örnek kod blokları ve pratik alıştırma
# fikirleri içerdiği için çalışma notu olarak kullanılabilir.
# ============================================================

# 1. Hello World! - adettendir
#print("hello world!")

# 2. List Comprehensions — 3 gün

# * Day 2: 1–20 arasındaki çift sayıları list comprehension ile oluştur.
# sonuc = [sayi for sayi in range(1,20) if sayi%2 == 0]
# print(sonuc)

# * Day 3: Bir kelime listesinden uzunluğu 5+ olanları seç.
# list = ['zeynep', 'yunus', 'alya', 'azra']
# sonuc = [i for i in list if len(i) >= 5]
# print(sonuc)

# * Day 4: [1, 2, 3, 4, 5] listesindeki sayıların karelerini oluştur.
# liste = [1, 2, 3, 4, 5]
# sonuc =[i*i for i in liste]
# print(sonuc) 

# 3. Lambda & Built-in Functions — 7 gün

# * Day 5: Lambda ile iki sayıyı çarp.
# sonuc = (lambda x, y: x * y)(2, 3)
# print(sonuc)

# * Day 6: map() ile sayı listesinin karelerini oluştur.
# liste = [1, 2, 3, 4, 5]
# sonuc = list(map(lambda a: a*a, liste))
# print(sonuc)

# * Day 7: filter() ile çift sayıları bul.
# liste = [1, 2, 3, 4, 5]
# sonuc = list(filter(lambda x: x%2 == 0, liste))
# print(sonuc)

# * Day 8: filter() ile 10’dan büyük sayıları bul.
# liste = [1, 2, 3, 5, 10, 15, 20]
# sonuc = list(filter(lambda x: x>10, liste))
# print(sonuc)

# * Day 9: sorted() ile kelimeleri sırala.
# list = ['zeynep', 'yunus', 'alya', 'azra']
# sonuc = sorted(list)
# print(sonuc)

# * Day 10: map() ile kelimelerin uzunluklarını bul.
# liste = ['zeynep', 'yunus', 'alya', 'azra']
# sonuc = list(map(lambda i: len(i), liste))
# print(sonuc)

# * Day 11: reduce() kullanarak listedeki sayıların toplamını bul.
# from functools import reduce
# liste = [1, 2, 3, 4, 5]
# sonuc = reduce(lambda x, y: x+y, liste)
# print(sonuc)

# 4. OOP — 10 gün

# * Day 12: Student class’ı oluştur, name ve age tut.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# a = Student("ayse", 18)
# print(a.name, a.age)
    
# * Day 13: Student içine introduce() methodu ekle.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         return f"Ad:{self.name} Yas:{self.age}"
# a = Student("ayse", 18)
# print(a.introduce())

# * Day 14: Car class’ı oluştur, marka ve model bilgisi alsın.
# class Car:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
# class CarAl:
#     def __init__(self):
#         self.liste = []
#     def kullanicidanAl(self):
#         marka = input("Marka bilgisi:" )
#         model = input("Model Bilgisi: ")
#         yeniListe = Car(marka, model)
#         self.liste.append(yeniListe)
#         print(self.liste)
#     def view(self):
#         for i in self.liste:
#             print(f"{i.marka} {i.model}")
# car = CarAl()
# car.kullanicidanAl()
# car.view()

# * Day 15: Car içine drive() methodu ekle.
# class Car:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
#         self.km = 0
#     def drive(self):
#         self.km += 1
#         print(self.km)
# class CarAl:
#     def __init__(self):
#         self.liste = []
#     def kullanicidanAl(self):
#         marka = input("Marka bilgisi:" )
#         model = input("Model Bilgisi: ")
#         yeniListe = Car(marka, model)
#         self.liste.append(yeniListe)
#         print(self.liste)
#     def view(self):
#         for i in self.liste:
#             print(f"{i.marka} {i.model}")
# car = CarAl()
# car.kullanicidanAl()
# car.view()
# car.liste[0].drive()
# car.liste[0].drive()
# car.liste[0].drive()

# * Day 16: Book class’ı oluştur ve 2 farklı kitap objesi yarat.
# class Book:
#     def __init__(self, writer, name, page):
#         self.writer = writer
#         self.name = name
#         self.page = page

# b = Book("matt haig", "hayat imkansiz", 300)
# print(b.writer, b.name, b.page)
# b1 = Book("a", "b", 200)
# print(b1.writer, b1.name, b1.page)

# * Day 17: Bir class’a class attribute ekle.
# class Book:
#     discount = 0.8
#     def __init__(self, writer, name, page, price):
#         self.writer = writer
#         self.name = name
#         self.page = page
#         self.price = price
#     def discounted_price(self):
#         return self.price * Book.discount

# b = Book("matt haig", "hayat imkansiz", 300, 400)
# print(b.writer, b.name, b.page)
# print(b.discounted_price())

# * Day 18: Bir class’a private attribute eklemeyi dene.
# class Book:
#     def __init__(self, writer, name, page, book_id):
#         self.writer = writer
#         self.name = name
#         self.page = page
#         self.__id = book_id
#     def get_id(self):
#         return self.__id

# b = Book("matt haig", "hayat imkansiz", 300, 58)
# print(b.writer, b.name, b.page, b.get_id())

# * Day 19: Animal → Dog inheritance yapısını kur.
# class Animal:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
        
# class Dog(Animal):
#     pass

# d = Dog("Gofret", "Dog", 3)
# print(f"{d.name} {d.breed} {d.age}")


# * Day 20: Animal içinde speak(), Dog içinde override edilmiş speak() yaz.
class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def speak(self):
        return "sound"
        
class Dog(Animal):
    def speak(self):
        return "hav hav"

d = Dog("Gofret", "Dog", 3)
print(f"{d.name} {d.breed} {d.age} {d.speak()}")

# * Day 21: BankAccount class’ı oluştur: deposit() ve withdraw() ekle.

# 5. Iterators & Generators — 4 gün

# * Day 22: Bir listenin iterator’ını oluştur ve next() kullan.
# * Day 23: Kendi iterator class’ını oluşturmayı dene.
# * Day 24: 1–10 arasında sayı üreten generator yaz.
# * Day 25: Sonsuz şekilde sıradaki sayıyı üreten generator yaz.

# 6. İleri Seviye Fonksiyonlar — 7 gün

# * Day 26: Bir fonksiyonu başka bir fonksiyona parametre olarak gönder.
# * Day 27: Bir fonksiyonun başka bir fonksiyon döndürmesini yap.
# * Day 28: Basit bir decorator yaz.
# * Day 29: Bir fonksiyonun çalışmasından önce "Starting..." yazdıran decorator yap.
# * Day 30: *args kullanan bir fonksiyon yaz.
# * Day 31: **kwargs kullanan bir fonksiyon yaz.
# * Day 32: Hem *args hem **kwargs alan bir fonksiyon yaz.

# 7. Regular Expressions — 3 gün

# * Day 33: Bir string içinde "python" kelimesini regex ile ara.
# * Day 34: Bir text içindeki bütün sayıları regex ile bul.
# * Day 35: Basit bir email adresini regex ile kontrol et.

# 8. CSV — 6 gün

# * Day 36: Python ile students.csv oluştur.
# * Day 37: CSV dosyasını okuyup satırları yazdır.
# * Day 38: CSV’den sadece belirli bir sütunu yazdır.
# * Day 39: CSV’ye yeni bir öğrenci ekle.
# * Day 40: CSV’deki öğrencilerin yaş ortalamasını hesapla.
# * Day 41: CSV’den belirli koşula uyan satırları filtrele.

# 9. JSON — 7 gün

# * Day 42: Python dictionary’sini JSON string’e çevir.
# * Day 43: JSON string’i Python dictionary’sine çevir.
# * Day 44: Bir dictionary’yi .json dosyasına kaydet.
# * Day 45: JSON dosyasını Python’da oku.
# * Day 46: JSON içindeki nested data’ya eriş.
# * Day 47: JSON’a yeni bir kayıt ekle.
# * Day 48: JSON’daki kayıtları bir koşula göre filtrele.

# 10. HTTP Requests — 6 gün

# * Day 49: Python ile bir URL’ye GET request at.
# * Day 50: Response’un status code’unu yazdır.
# * Day 51: Response’un text içeriğini yazdır.
# * Day 52: Bir API’den JSON response al.
# * Day 53: API response’undan tek bir bilgiyi çek.
# * Day 54: Hatalı request durumunu try/except ile yakala.

# 11. Web Scraping — 7 gün

# * Day 55: Bir web sayfasının HTML’ini request ile al.
# * Day 56: BeautifulSoup ile sayfanın title’ını bul.
# * Day 57: Sayfadaki bütün <a> taglerini bul.
# * Day 58: Bütün linkleri listele.
# * Day 59: Sayfadaki başlıkları (h1/h2) çek.
# * Day 60: Çektiğin başlıkları bir listeye koy.
# * Day 61: Çektiğin verileri CSV’ye kaydet.

# 12. Veri Tabanı — 13 gün

# Burada özellikle SQL + Python bağlantısını oturtmanı istiyorum.

# * Day 62: SQLite database oluştur.
# * Day 63: students table oluştur.
# * Day 64: Table’a bir öğrenci ekle.
# * Day 65: Bütün öğrencileri SELECT et.
# * Day 66: Sadece belirli bir öğrenciyi WHERE ile bul.
# * Day 67: Bir öğrencinin bilgisini UPDATE et.
# * Day 68: Bir öğrenciyi DELETE et.
# * Day 69: Python’dan database’e bağlan.
# * Day 70: Python ile SQL INSERT çalıştır.
# * Day 71: Python ile SQL SELECT çalıştır.
# * Day 72: Python’dan gelen database sonuçlarını loop ile yazdır.
# * Day 73: try/except ile database hatası yakala.
# * Day 74: Mini proje: Student CRUD yapmaya başla.

# 13. Socket Programming — 3 gün

# * Day 75: Basit bir socket oluştur.
# * Day 76: Localhost’a connection kurmayı dene.
# * Day 77: Client → Server "Hello" mesajı gönder.

# 14. Thread & Process — 4 gün

# * Day 78: Bir thread oluştur ve function çalıştır.
# * Day 79: Aynı anda iki thread çalıştır.
# * Day 80: Thread’lerin çalışma sırasını gözlemle.
# * Day 81: Basit bir multiprocessing örneği oluştur.

# 15. Entegrasyon — 3 gün

# * Day 82: API’den JSON çek → Python dictionary’sine çevir.
# * Day 83: API’den veri çek → CSV’ye kaydet.
# * Day 84: Mini Data Pipeline: API → JSON → Python → SQLite.