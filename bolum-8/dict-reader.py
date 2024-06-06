import csv

with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    for i in csv_reader:
        if i["Category"] == "Telefon" and float(i["Rating"]) >= 4.5:
            print(i["ProductName"], i["Price"])