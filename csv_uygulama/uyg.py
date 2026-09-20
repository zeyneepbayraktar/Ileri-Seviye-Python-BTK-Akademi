#Online yemek siparisi veren kac kisi var
#Online yemek siparisi veren ogrencileri listeleyin
#20-30 yas araligindaki kisilerin konum listesini hazirlayiniz

import csv
from pathlib import Path

csv_path = Path(__file__).with_name("onlinefoods.csv")

with csv_path.open() as file:
    csv_reader = csv.reader(file)
    liste = list(csv_reader)
    print(len(liste) - 1)

with csv_path.open() as file:
    csv_reader = csv.DictReader(file)
    adet = len([user for user in csv_reader if user["Occupation"] == "Student"])
    print(adet)

with csv_path.open() as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        if float(i["Age"]) >= 20 and float(i["Age"]) <= 30:
            print(i["latitude"], i["longitude"])

    