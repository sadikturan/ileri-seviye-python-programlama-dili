def selamlama(fn):
    def inner(ad):
        print("hoş geldiniz")
        fn(ad)
        print("görüşmek üzere")
    return inner

@selamlama
def gunaydin(ad):
    print(f"günaydın benim adım {ad}")

@selamlama
def iyigunler(ad):
    print(f"iyi günler benim adım {ad}")

# g = selamlama(gunaydin)
# i = selamlama(iyigunler)

# g()
# i()
    
gunaydin("Ali")
iyigunler("Sadık")