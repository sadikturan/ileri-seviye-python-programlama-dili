sayilar = [1,2,3,4,5]
sayilar_str = ["1","2","3","4","5"]
isimler = ["ali","hasan","ayşe","zeynep"]
kullanicilar = [
    {"ad":"ali", "soyad":"yılmaz"},
    {"ad":"ahmet", "soyad":"cengiz"}
]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)

# def kareAl(sayi):
#     return sayi ** 2

# int("2") # 2

sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
sonuc = list(map(int, sayilar_str))
sonuc = list(map(str.capitalize, isimler))
sonuc = list(map(lambda kisi: kisi["ad"], kullanicilar))

print(sonuc)

