# ============================================================
# CSV WRITER
# CSV dosyasına veri yazma işlemini gösterir. Yeni dosya oluşturup
# verileri dönüştürerek kaydetmek için csv.writer kullanılır.
# ============================================================

import csv

# with open("arabalar.csv", "w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows([["Marka", "Model"], ["Marka1", "Model1"], ["Marka2", "Model2"]])

with open("urunler.csv") as file:
    csv_reader = csv.reader(file)
    with open("yeniUrunler.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        for urun in csv_reader:
            csv_writer.writerow([u.upper() for u in urun])

