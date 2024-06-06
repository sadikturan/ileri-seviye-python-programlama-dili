class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    # def set_price(self, value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #         raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    # def get_price(self):
    #     return self._price


p = Product("IPhone 16", 80000)

print(p.price)
p.price = -90000
print(p.price)

# p.set_price(70000)
# print(p.get_price())    => p.price, p.price = 70000
# print(p.name, p.price)