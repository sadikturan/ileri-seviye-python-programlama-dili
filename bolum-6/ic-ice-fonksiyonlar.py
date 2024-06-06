# def selam(isim):
#     return f"selam, {isim}"

# # print(selam("Çınar"))
# # print(selam)

# merhaba = selam

# print(selam)
# print(merhaba)

# del selam
# print(merhaba)

# # print(selam("Çınar"))
# print(merhaba("Çınar"))


# def outer(number):
#     def inner(number):
#         print(number)

#     inner(number)

# outer(10)

def faktoriyel(sayi):

    if not isinstance(sayi, int):
        raise TypeError("number must be an int")
    
    if not sayi >= 0:
        raise ValueError("number must be zero or positive")

    def inner_faktoriyel(sayi):
        if sayi <= 1:
            return 1
        
        return sayi * inner_faktoriyel(sayi - 1)
    
    return inner_faktoriyel(sayi)

sonuc = faktoriyel(5)
try:
    sonuc = faktoriyel("4")
    print(sonuc)
except Exception as ex:
    print(ex)