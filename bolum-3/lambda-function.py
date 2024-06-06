# lambda arguments: expression

def kareAl(a):
    return a ** 2

sonuc = kareAl(5)

sonuc = (lambda a: a ** 2)(3)

kareAl = lambda a: a ** 2

sonuc = kareAl(4)

toplama = lambda a,b,c: a + b + c

sonuc = toplama(1,2,3)

def myFunc(n):
    return lambda a: a * n

carpma2 = myFunc(2)
carpma3 = myFunc(3)
carpma5 = myFunc(5)

sonuc = carpma2(3)
sonuc = carpma3(5)
sonuc = carpma5(5)

print(sonuc)