# Python İleri Seviye - Fonksiyonel Yapılar ve List Comprehension

BTK Akademinin İleri Seviye Python eğitimini izlerken tuttuğum notlardan derlenmiş, açıklamalar ve alıştırılabilir örnekler. Her dosya tek bir konuya odaklanır, yorum satırları ile açıklanmıştır ve baştan sona çalıştırıldığında ilgili örneklerin çıktısını terminalde görebilirsiniz.

## Konular

| Sıra | Dosya | Konu |
|---|---|---|
| 1 | [listcomprehension.py](listcomprehension.py) | List comprehension temelleri (klasik döngü ile karşılaştırma, koşullu kullanım) |
| 2 | [listcomprehension_uygulama.py](listcomprehension_uygulama.py) | List/dict comprehension uygulama soruları |
| 3 | [lambdafonksiyonu.py](lambdafonksiyonu.py) | Lambda (anonim) fonksiyonlar ve closure |
| 4 | [mapfonsiyonu.py](mapfonsiyonu.py) | `map()` ve `filter()` ile veri dönüştürme/filtreleme |
| 5 | [anyVeAllFonsiyonu.py](anyVeAllFonsiyonu.py) | `any()` ve `all()` ile koşul kontrolü |
| 6 | [sortedfonksiyounu.py](sortedfonksiyounu.py) | `sorted()` ile sıralama |
| 7 | [maxfonksiyonu.py](maxfonksiyonu.py) | `max()` / `min()` ve `key` parametresi |
| 8 | [sumveround.py](sumveround.py) | `sum()` ile toplama, `round()` ile yuvarlama |

## Nasıl çalıştırılır

Python 3 kurulu olması yeterli, ekstra bir bağımlılık yok.

```bash
python3 listcomprehension.py
python3 lambdafonksiyonu.py


## Öğrenilen ana kavramlar

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
