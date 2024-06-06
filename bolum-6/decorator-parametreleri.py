def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return inner

@double
def merhaba():
    print("merhaba")

@double
def selam(isim):
    print("selam ", isim)

@double
def iyigunler():
    return "iyi günler"

merhaba()
selam("Ali")
print(iyigunler())