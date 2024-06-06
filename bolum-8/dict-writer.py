import csv

# with open("urunler2.csv","w", newline='') as file:
#     headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
#     csv_writer = csv.DictWriter(file, headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Id": 1,
#         "ProductName":"IPhone 14", 
#         "Price": 40000,
#         "IsActive": True,
#         "Category":"Telefon",
#         "Rating": 4.6
#     })

#     csv_writer.writerow({
#         "Id": 2,
#         "ProductName":"IPhone 15", 
#         "Price": 50000,
#         "IsActive": True,
#         "Category":"Telefon",
#         "Rating": 4.6
#     })

#     csv_writer.writerows([
#         {
#             "Id": 1,
#             "ProductName":"IPhone 14", 
#             "Price": 40000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 4.6
#         },
#         {
#             "Id": 2,
#             "ProductName":"IPhone 15", 
#             "Price": 40000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 4.6
#         },{
#             "Id": 3,
#             "ProductName":"IPhone 16", 
#             "Price": 40000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 4.6
#         },
#     ])


# with open("urunler2.csv","a", newline='') as file:
#     headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
#     csv_writer = csv.DictWriter(file, headers)
#     csv_writer.writerow({
#         "Id": 4,
#         "ProductName":"IPhone 17", 
#         "Price": 40000,
#         "IsActive": True,
#         "Category":"Telefon",
#         "Rating": 4.6
#     })

def price_tax(price):
    return float(price) * 1.20
    
with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    urunler = list(csv_reader)

    with open("urunler3.csv","w", newline='') as file:
        headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
        csv_writer = csv.DictWriter(file, headers)
        csv_writer.writeheader()

        for u in urunler:
            csv_writer.writerow({
                "Id": u["Id"],
                "ProductName":u["ProductName"], 
                "Price": price_tax(u["Price"]), 
                "IsActive": u["IsActive"], 
                "Category":u["Category"], 
                "Rating": u["Rating"], 
            }) 