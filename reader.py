# ============================================================
# CSV READER
# CSV dosyasını satır satır okuyup istenen koşullara göre filtreleme
# yapmayı öğreniriz. csv.reader ile tablolara benzer veri okuruz.
# ============================================================

# with open("urunler.csv") as file:
#     print(file.read())

import csv
with open("urunler.csv") as file:
    csv_reader = csv.reader(file)

    # print(csv_reader)
    # print(list(csv_reader))

    next(csv_reader)
    for i in csv_reader:
        if i[3] == "True":
            print(f"id: {i[0]}, name:{i[1]}")

