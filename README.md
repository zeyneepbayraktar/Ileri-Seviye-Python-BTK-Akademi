# Python İleri Seviye

BTK Akademinin İleri Seviye Python eğitimini izlerken tuttuğum notlardan derlenmiş, açıklamalar ve alıştırılabilir örnekler. Her dosya tek bir konuya odaklanır, yorum satırları ile açıklanmıştır ve baştan sona çalıştırıldığında ilgili örneklerin çıktısını terminalde görebilirsiniz.

## 2. List Comprehensions

| Ders | Dosya | Konu |
|---|---|---|
| 2.1 - 2.2 | [listcomprehension.py](listcomprehension.py) | List comprehension nedir (klasik döngü ile karşılaştırma) ve koşullu durumlar |
| 2.3 | [listcomprehension_uygulama.py](listcomprehension_uygulama.py) | Uygulama: list/dict comprehension soruları |

## 3. Lambda ve Built-in Fonksiyonlar

| Ders | Dosya | Konu |
|---|---|---|
| 3.1 | [lambdafonksiyonu.py](lambdafonksiyonu.py) | Lambda (anonim) fonksiyonlar ve closure |
| 3.2 - 3.3 | [mapfonsiyonu.py](mapfonsiyonu.py) | `map()` ile dönüştürme, `filter()` ile filtreleme ve ikisini zincirleme |
| 3.4 | [anyVeAllFonsiyonu.py](anyVeAllFonsiyonu.py) | `any()` ve `all()` ile koşul kontrolü |
| 3.5 | [sortedfonksiyounu.py](sortedfonksiyounu.py) | `sorted()` ile sıralama |
| 3.6 | [maxfonksiyonu.py](maxfonksiyonu.py) | `min()` / `max()` ve `key` parametresi |
| 3.7 | [sumveround.py](sumveround.py) | `sum()` ile toplama, `round()` ile yuvarlama |

## 4. Nesne Yönelimli Programlama

| Ders | Dosya | Konu |
|---|---|---|
| 4.1 | [classConstructors.py](classConstructors.py) | Class ve constructor (`__init__`), instance oluşturma |
| 4.2 | [instanceMethods.py](instanceMethods.py) | Instance methodlar, `self` ile nesnenin verisini okuma/değiştirme |
| 4.3 | [classAttributes.py](classAttributes.py) | Class attribute vs instance attribute, `__dict__`, nesne sayacı |
| 4.4 | [classMethods.py](classMethods.py) | `@classmethod`, `cls` ve alternatif constructor |
| 4.5 | [shoppingCart.py](shoppingCart.py) | Uygulama: alışveriş sepeti (CartItem + Coupon + ShoppingCart) |
| 4.6 | [kalitim.py](kalitim.py) | Kalıtım (inheritance), parent/child class, `pass` ile boş alt class |
| 4.7 | [childClass.py](childClass.py) | `super()` ile üst class constructor'ı, method override |
| 4.8 | [properties.py](properties.py) | `@property`, getter/setter ve encapsulation |
| 4.9 | [specialmethods.py](specialmethods.py) | Special (dunder) methodlar: `__repr__`, `__len__` |

> 4.10 Meta Class dersi henüz izlenmedi.

## Günlük soru challenge

[everyday1questionchallange/](everyday1questionchallange/) klasöründe her gün bir soru çözme planı ve çözümleri var:
[1.py](everyday1questionchallange/1.py) içinde konu konu (list comprehension, lambda, OOP, generator, decorator, regex, CSV, JSON, HTTP, web scraping, veritabanı, socket, thread) 84 günlük soru listesi ve çözülenlerin kodu bulunuyor.

## Nasıl çalıştırılır

Python 3 kurulu olması yeterli, ekstra bir bağımlılık yok.

```bash
python3 listcomprehension.py
python3 classConstructors.py
python3 shoppingCart.py
```

## Öğrenilen ana kavramlar

### List comprehension, lambda ve built-in fonksiyonlar

- **List comprehension**: `[ifade for eleman in iterable if kosul]` kalıbıyla
  döngüleri tek satıra indirmek; filtreleme (`if`) ile değer dönüştürmeyi
  (`if/else`) birbirinden ayırmak.
- **Lambda**: İsimsiz, tek satırlık fonksiyonlar; bir fonksiyondan lambda
  döndürerek closure oluşturmak.
- **map / filter**: Bir iterable'daki her elemana fonksiyon uygulamak (`map`)
  ya da koşulu sağlayanları süzmek (`filter`); ikisini zincirleyerek kullanmak.
- **any / all**: Bir koleksiyondaki elemanların "en az biri" ya da "hepsi"
  bir koşulu sağlıyor mu diye kontrol etmek.
- **sorted / max / min**: `key` parametresiyle özel bir kritere göre
  sıralama veya en büyük/en küçük değeri bulma.
- **sum / round**: Sayısal verilerde toplam ve ortalama hesaplama, sonucu
  `round()` ile okunabilir hale getirme.

### Nesne yönelimli programlama

- **Class ve constructor**: Class bir şablondur; `__init__` nesne
  oluşturulurken otomatik çalışır ve `self.xxx` ile instance attribute'ları
  belirler.
- **Instance method**: İlk parametresi `self` olan, nesnenin kendi verisi
  üzerinde çalışan methodlar (`calculate_total`, `apply_discount`).
- **Class attribute**: Class gövdesinde tanımlanan, tüm nesnelerin paylaştığı
  değer (`discount_rate`, `item_count`); instance attribute ise her nesneye
  özeldir ve `__dict__` içinde görünür.
- **Class method**: `@classmethod` + `cls` ile class'ın kendisi üzerinde
  çalışan methodlar; metinden nesne üreten alternatif constructor yazmak.
- **Kalıtım**: `class Alt(Ust)` ile ortak özellikleri devralmak, kod
  tekrarını önlemek; alt class gövdesi boşsa `pass` yazmak.
- **super() ve override**: `super().__init__(...)` ile üst class'ın
  constructor'ını çalıştırıp ortak alanları tekrar yazmamak; aynı isimli
  methodu alt class'ta yeniden yazmak (override).
- **Property**: `@property` / `@price.setter` ile attribute'a doğrudan
  erişimi kontrol altına almak, atama sırasında doğrulama (negatif fiyat
  engelleme) yapmak.
- **Special methodlar**: `__repr__` ile nesnenin okunabilir metin gösterimi,
  `__len__` ile `len()` desteği.
