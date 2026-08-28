# Python İleri Seviye

BTK Akademinin ileri seviye Python eğitiminde izlenen konular, örnekler ve pratik alıştırmaların toplandığı bir çalışma notları deposudur. Her dosya tek bir konuyu anlatır; dosyaların başında kısa açıklamalar bulunur ve kodlar mantığı değiştirmeden çalıştırılabilir şekilde hazırlanmıştır.

## Proje içeriği

### 2. List Comprehensions

| Dosya | Konu |
|---|---|
| [listcomprehension.py](listcomprehension.py) | List comprehension mantığı, klasik döngü ile karşılaştırma ve koşullu örnekler |
| [listcomprehension_uygulama.py](listcomprehension_uygulama.py) | Uygulama soruları ve pratik örnekler |

### 3. Lambda ve built-in fonksiyonlar

| Dosya | Konu |
|---|---|
| [lambdafonksiyonu.py](lambdafonksiyonu.py) | Lambda fonksiyonlar ve closure örnekleri |
| [mapfonsiyonu.py](mapfonsiyonu.py) | map() ve filter() kullanım örnekleri |
| [anyVeAllFonsiyonu.py](anyVeAllFonsiyonu.py) | any() ve all() ile koşul kontrolü |
| [sortedfonksiyounu.py](sortedfonksiyounu.py) | sorted() ile sıralama |
| [maxfonksiyonu.py](maxfonksiyonu.py) | min() / max() ve key parametresi |
| [sumveround.py](sumveround.py) | sum() ve round() örnekleri |

### 4. Nesne yönelimli programlama

| Dosya | Konu |
|---|---|
| [classConstructors.py](classConstructors.py) | Class ve constructor yapısı |
| [instanceMethods.py](instanceMethods.py) | Instance methodlar ve self kullanımı |
| [classAttributes.py](classAttributes.py) | Class attribute ve instance attribute farkı |
| [classMethods.py](classMethods.py) | @classmethod ve cls kullanımı |
| [shoppingCart.py](shoppingCart.py) | Alışveriş sepeti uygulaması |
| [kalitim.py](kalitim.py) | Kalıtım nedir ve nasıl kullanılır |
| [childClass.py](childClass.py) | super() ve method override |
| [properties.py](properties.py) | @property ve encapsulation |
| [specialmethods.py](specialmethods.py) | __repr__ ve __len__ gibi dunder methodlar |

### 5. İterator, generator ve bellek yönetimi

| Dosya | Konu |
|---|---|
| [customIterator.py](customIterator.py) | Kendi iterator sınıfı örneği |
| [iterableAndIterators.py](iterableAndIterators.py) | Iterable ve iterator farkı |
| [generators.py](generators.py) | Generator kavramı ve kullanım örnekleri |
| [BellekYonetimi_uyg.py](BellekYonetimi_uyg.py) | Bellek tüketimi, generator ve Fibonacci örnekleri |

### 6. Ek örnekler ve mini projeler

| Dosya | Konu |
|---|---|
| [metaClass.py](metaClass.py) | Metaclass örnekleri |
| [ExpenseTrackerCLI.py/main.py](ExpenseTrackerCLI.py/main.py) | Harcama takip CLI uygulaması |
| [everyday1questionchallange/1.py](everyday1questionchallange/1.py) | Günlük soru challenge listesi ve örnek çözümler |

### 7. İleri düzey fonksiyonlar ve decorator

| Dosya | Konu |
|---|---|
| [ileriDuzeyFonksiyonlar.py](ileriDuzeyFonksiyonlar.py) | İç içe fonksiyonlar, fonksiyondan fonksiyon döndürme ve fonksiyonları parametre olarak kullanma |
| [decoratorFonksiyonlar.py](decoratorFonksiyonlar.py) | Decorator mantığı, parametreli decorator ve performans ölçüm örnekleri |
| [decorator_uygulama.py](decorator_uygulama.py) | Speed test decorator uygulaması |

## Çalıştırma

Python 3 kurulu olması yeterlidir. Ek bağımlılık gerekmez.

```bash
python3 listcomprehension.py
python3 lambdafonksiyonu.py
python3 shoppingCart.py
python3 ExpenseTrackerCLI.py/main.py
```

## Öğrenilen ana kavramlar

- List comprehension ile kısa ve okunaklı veri üretimi
- Lambda fonksiyonları ve built-in fonksiyonların kombinasyonu
- map(), filter(), any(), all(), sorted(), min(), max(), sum(), round()
- Class, instance, inheritance, property ve special methods
- Iterable, iterator ve generator yapısı
- Bellek verimliliği ve çıktının karşılaştırılması
- İleri düzey fonksiyonlar ve decorator kullanımı
- Kendi mini uygulama ve CLI tasarımı

## Not

Tüm örnekler ders sırasında öğrenilen konuların uygulanması için hazırlanmıştır. Her dosya, benzer konu anlatımı mantığıyla yorum satırları ve örnek açıklamalar içerir. 