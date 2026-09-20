import csv 

# with open("urunler2.csv", "w") as file:
#     headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
#     csv_writer = csv.DictWriter(file, headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Id": 1,
#         "ProductName": "Iphone 14",
#         "Price": 40000,
#         "IsActive": True,
#         "Category": "Telefon",
#         "Rating": 4.6
#     })
#     csv_writer.writerow({
#         "Id": 2,
#         "ProductName": "Iphone 15",
#         "Price": 50000,
#         "IsActive": True,
#         "Category": "Telefon",
#         "Rating": 4.6
#     })

def price_tex(price):
    return float(price) * 1.20

with open("urunler.csv") as file:
    csv_reader =csv.DictReader(file)
    urunler = list(csv_reader)
    with open("urunler3.csv", "w") as file:
        headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
        csv_writer = csv.DictWriter(file, headers)
        csv_writer.writeheader()

        for u in urunler:
            csv_writer.writerow({
                "Id": u["Id"],
                "ProductName": u["ProductName"],
                "Price": u["Price"],
                "IsActive": u["IsActive"],
                "Category": u["Category"],
                "Rating": u["Rating"]
            })
            