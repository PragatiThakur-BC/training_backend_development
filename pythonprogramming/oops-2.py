from dataclasses import dataclass


# MULTIPLE INHERITANCE
class Base1:
    def __init__(self):
        self.name = "Bella"
        print("Base1")


class Base2:
    def __init__(self):
        self.age = 23
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def printing(self):
        print(self.name, self.age)


x = Derived()
x.printing()


# ENCAPSULATION
# PRIVATE VARIABLES and PROTECTED VARIABLES
class A:
    def __init__(self):
        self.g = None
        self.a = 10
        self.__z = 42
        self._b = 60

    def greeting(self):
        self.g = "Hello to class A"
        print("A")


class B(A):
    def __init__(self):
        self.d = 15
        print("B")
        A.__init__(self)
        print("calling protected member of class A in B: ", self._b)


obj1 = B()
obj1.greeting()
print("from class a: accessing a:- ", obj1.a)
print("from class a: accessing g:- ", obj1.g)
# print("from class a: accessing d(private):- ", obj1.z) This will produce and error as z is defined as private


# POLYMORPHISM
# Built-in eg-- Len()
print(len("apple"))  # the argument is string and single value
print(len([1, 2, 3, 4]))  # the argument is a list


# Polymorphism with function - method overloading
def add(x, y, z=0):
    return x+y+z


print(add(2, 3))  # takes the default value
print(add(2, 3, 4))  # overwrites the default value with whatever argument value we have passed


# Polymorphism with class methods -  method overriding
class Usa:
    def currency(self):
        print("USA - Dollar")

    def capital(self):
        print("Washington DC is capital of USA")

    def type(self):
        print("developed country")


class SouthKorea:
    def currency(self):
        print("Skorea- Korean WON")

    def capital(self):
        print("Seoul is capital of Skorea")

    def type(self):
        print("developed country")


u = Usa()
sk = SouthKorea()
for country in (u, sk):
    country.currency()
    country.capital()
    country.type()


# Polymorphism with inheritance
class Animals:
    def intro(self):
        print("Animal class")

    def legs(self):
        print("Different Animal categories have different legs")


class Dog(Animals):
    def greeting(self):
        print("Wags tail")
        Animals.__init__(self)

    def legs(self):
        print("Dogs have 4 legs")


d = Dog()
d.greeting()
d.legs()


# CLASS/STATIC VARIABLES and INSTANCE VARIABLE
class CSE:
    section = "Computer Science Engineering"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def details(self):
        print("Department: ", self.section)
        print("Student name: " + self.name + " Roll.no: " + self.roll)


s1 = CSE("Bella", '1')
s2 = CSE("Drake", '2')
s1.details()
s2.section = "Electrical Engineering"
s2.details()
s2.name = "Drake - Johnson"
s2.details()
s1.details()  # only the details of s2 section are changes for class variable and not for s1.


# Bundling together a few named data items.
# The idiomatic approach is to use dataclasses for this purpose import dataclass for this
@dataclass
class Student:
    name: str
    department: str
    roll_no: int
    grade: float


s1 = Student("Bella", "CSE", 53, 9.8)
print(s1.name, s1.grade)


# class method
class MiniClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


obj = MiniClass(19)
print(obj.get_value())


# Static Method
class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_min_value(x, y):
        return min(x, y)


obj1 = MyClass(10)
print(obj1.get_min_value(20, 15))
print(MyClass.get_min_value(30, 12))

