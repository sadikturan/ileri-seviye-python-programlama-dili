# with open("urunler.csv") as file:
#     print(file.read())

import csv

with open("urunler.csv") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    # liste = list(csv_reader)
    # print(liste[1])
    next(csv_reader)
    for i in csv_reader:
        if i[3] == "True":
            print(f"id: {i[0]}, ürün adı: {i[1]}")

# DictReader