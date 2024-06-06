class CartItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name,price,quantity)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

c1 = Coupon("code1", 0.8)
c2 = Coupon("code2", 0.7)
c3 = Coupon("code3", 0.9)
 
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("Kitap", 500, 2)

class ShoppingCart:
    coupon_list = [c1, c2, c3]

    def __init__(self, liste):
        self.liste = liste

    def add_item(self, item):
        self.liste.append(item)

    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")

    def calculate_totals(self):
        return sum([item.calculate_total() for item in self.liste])
    
    def remove_item(self, cart_item):
        self.liste = [item for item in self.liste if item != cart_item]

    def clear(self):
        self.liste = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]
    
    @classmethod
    def get_coupon(cls, code):
        return next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))
    
    def apply_coupon(self, code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"geçersiz kupon kodu: {code}")
        
        coupon = ShoppingCart.get_coupon(code)

        for index in range(0, len(self.liste)):
            self.liste[index].price = self.liste[index].price * coupon.discount

sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_items()
        
print(sc.calculate_totals())
        
# sc.remove_item(item1)

# sc.display_items()
        
# sc.clear()

# sc.display_items()

# sc.apply_coupon("code1")
        
# print(sc.calculate_totals())
        
# ShoppingCart.get_coupons()
# ShoppingCart.get_coupon("code1")
sc.apply_coupon("code2")  

print(sc.calculate_totals())
