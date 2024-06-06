# class Test():
#     pass

# class BaseClass():
#     def show(self):
#         return "merhaba"
    
# def add_attribute(self):
#     self.b = 10

# Test = type("Test", (BaseClass,), {"a":5, "add_attribute": add_attribute})
# t = Test()

# sonuc = Test()
# sonuc = Test
# sonuc = type(Test)
# # sonuc = type(2)
# # sonuc = type(int)
# # sonuc = type("2")
# # sonuc = type(str)
# sonuc = t.show()
# sonuc = t.a
# t.add_attribute()
# sonuc = t.b

# print(sonuc)



class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)
    
class Person(metaclass=Meta):
    x = 5
    y = 10
    _age = 40

    def hello(self):
        print("merhaba")

p = Person()

sonuc = p.X
sonuc = p.Y
sonuc = p._age

print(sonuc)