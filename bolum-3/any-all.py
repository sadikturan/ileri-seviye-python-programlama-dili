# any all

sonuc = all([True,True,False])
sonuc = all([True,True,True])
sonuc = any([True,True,True])
sonuc = any([True,True,False])
sonuc = any([False,False,False])

# And => True and True => all()
# Or  => True or False => any()

sayilar = [1,3,5,7,6,52,0]

sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = any([bool(sayi) for sayi in sayilar])
sonuc = all([sayi % 2 == 0 for sayi in sayilar])
sonuc = any([sayi % 2 == 0 for sayi in sayilar])

users = ["ahmet","çınar","hasan"]

sonuc = all([user[0] == "a" for user in users])
sonuc = any([user[0] == "a" for user in users])

print(sonuc)