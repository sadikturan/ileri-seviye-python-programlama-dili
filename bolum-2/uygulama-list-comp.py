# 1- (1-100) arasındaki sayılardan 12' e tam bölünebilen sayı listesini oluşturunuz.

sonuc = [i for i in range(1, 101) if i % 3 == 0 if i % 4 ==0]

# 2- Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
# text = "Hello 12345 World" => [1,2,3,4,5]

text = "Hello 12345 World"
sonuc = [i for i in text if i.isdigit()]

# 3- Sicakliklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında "buzlanma tehlikesi" yazınız.
# sicakliklar = [20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

sicakliklar = [20,15,0,-5,-2] 
sonuc = [i if i >= 4 else "Buzlanma Tehlikesi" for i in sicakliklar]

# 4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.

ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80] 
# => "{'ahmet': 60, 'canan': 80}"

# [("ali", 50), ("ahmet", 60), ("canan", 80)]
liste = [(ogrenciler[i], notlar[i]) for i in range(0, len(ogrenciler))]
liste_dict = { key:value for (key, value) in liste if value > 50}

# 5- For döngüsüyle yazılan uygulamayı list comprehension ile yazınız.
 
sonuc = [] 
# 0 - 0
# 0 - 1
# 0 - 2
# 1 - 0
# 1 - 1
# 1 - 2

for x in range(3):
    for y in range(3):
        for z in range(3):
            sonuc.append((x,y,z))

sonuc = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
