# iterable
# iterator

sayilar = [1,2,3,4,5,6]

iterator = iter(sayilar)

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break

# print(next(iterator))
# s = "BTK AKADEMİ"
# a = 10

# for i in a:
#     print(i)
