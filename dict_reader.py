# ============================================================
# CSV DICT READER
# csv.DictReader ile sütun adlarıyla çalışırız. Böylece veri alanını
# kolon adı üzerinden hızlı ve okunaklı şekilde filtreleyebiliriz.
# ============================================================

import csv
with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        if i["Category"] == "Telefon" and float(i["Rating"]) >= 4.5:
            print(i["ProductName"], i["Price"])

# import csv
# with open("urunler.csv") as file:
#     csv_reader = csv.DictReader(file, delimiter="|") #eger , degil baska bir seyle ayrildisa
#     for i in csv_reader:
#         if i["Category"] == "Telefon" and float(i["Rating"]) >= 4.5:
#             print(i["ProductName"], i["Price"])