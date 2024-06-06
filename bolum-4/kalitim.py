class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass    

class Teacher(Person):
    pass

p1 = Person("Sadık","Turan", 40)
p1.intro()

s1 = Student("Çınar","Turan",7)
s1.intro()

t1 = Teacher("Ali","Korkmaz",35)
t1.intro()