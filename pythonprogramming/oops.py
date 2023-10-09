# LOCAL AND GLOBAL SCOPES OF VARIABLE
def to_check_scope():
    def local_scope():
        data = "local data"

    def nonlocal_scope():
        nonlocal data
        data = "nonlocal data"

    def global_scope():
        global data
        data = "global data"

    data = "test data"
    local_scope()
    print("After local scope assignment local scope data : ", data)
    nonlocal_scope()
    print("after non-local scope assignment data: ", data)
    global_scope()
    print("After global scope assignment data: ", data)


to_check_scope()
print("Checking the global scope data: ", data)

"""
local assignment (which is default) did not change scope_test's binding of data.
The nonlocal assignment changed scope_test's binding of data,
and the global assignment changed the module-level binding.
"""


# CLASS -INTRO
# ATTRIBUTE REFERENCES
class MyClass:
    """A simple example of class"""
    i = 123

    def f(self):
        return "Hello World"


# MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object.
# x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not.
# But x.f is not the same thing as MyClass.f — it is a method object, not a function object.
print(MyClass.i)
print(MyClass.f(''))
# Instantiating the class with help of x(object of class)
print(MyClass.__doc__)
x = MyClass()
print(x.f(), x.i)


# Understanding __init__ method
class Complex:
    def __init__(self, realpart, imagpart):
        """The __init__() method takes the object itself (referred to as self) as the first argument,
        followed by any other arguments required to initialize the object's attributes"""
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, 4.0)
print(x.r, x.i)


# METHOD OBJECTS - not necessary to call a method right away:
# x.f is a method object, and can be stored away and called at a later time.
"""
the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a
list of n arguments is equivalent to calling the corresponding function with an argument
list that is created by inserting the method’s instance object before the first argument.
"""
xf = x.f
n = 1
while n < 5:
    print(xf())
    n = n + 1


# CLASS AND INSTANCE VARIABLES
class Car:
    wheel = 4  # class variable shared by all instances

    def __init__(self, brand):
        self.brand = brand  # instance variable unique to each instance


h = Car("Honda")
d = Car("Duster")
print("Honda wheel: ", h.wheel)
print("Duster Wheel: ", d.wheel)
print("Car1-Name: ", h.brand)
print("Car2-Name: ", d.brand)


# RANDOM REMARKS
class Region:
    """If the same attribute name occurs in both an instance and in a class,
    then attribute lookup prioritizes the instance"""
    location = "Mumbai"
    Direction = "West"


w = Region()
print(w.Direction, w.location)
n = Region()
n.Direction = "NORTH"
print(n.Direction, n.location)


# FUNCTION OUTSIDE THE CLASS and accessing them as method
def add(self, n1, n2):
    """
    The function definition does not have to be written within the class definition itself.
    the function object can be assigned to a local variable within the class,
    and this will still define a method for instances of that class
    """
    return n1 + n2


class Addition:
    a = add
    """
    here a, greetings, h are all attributes of class
    and instances of h and greetings are same.
    """
    def greetings(self):
        return "Hello world"
    h = greetings


summation = Addition()
print(summation.a(10, 15))
print(summation.greetings())
print(summation.h())


# METHODS CALLING OTHER METHODS - by using method attributes of the self argument
class Basket:
    def __init__(self):
        self.basket = []

    def add_once(self, x):
        self.basket.append(x)
        return self.basket

    def add_twice(self, x):
        self.add_once(x)
        self.add_once(x)
        return self.basket

    def pop_data(self):
        self.basket.pop()
        return self.basket


b = Basket()
b.add_once(1)
b.add_twice(2)
b.add_twice(3)
print("After addition of data once and twice", b.basket)
b.pop_data()
print("After data is removed(pop)", b.basket)
b.pop_data()
print("Another pop:", b.basket)


# INHERITANCE
# BASE CLASS AND SINGLE INHERITANCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


# CHILD CLASS
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        # inheriting properties of Base class
        super().__init__(name, age)

    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)


s1 = Person("Bella", 23)
s2 = Student("Rick", 22, "10-03-2000")
print("Student 1 with method of parent class: ")
s1.display()
print("Student 2 with method of child class: ")
s2.displayInfo()
print("Student 2 with method of parent class: ")
s2.display()


# DIFFERENT INHERITANCES
# MULTIPLE INHERITANCE
class StudentGrade(Student):
    def __init__(self, name, age, dob, grade):
        self.gname = name
        self.gage = age
        self.gdob = dob
        self.grade = grade
        # inheriting the properties of student class
        super().__init__(name, age, dob)

    def display_student_grade(self):
        print(self.gname, self.gage, self.gdob, self.grade)


sg = StudentGrade("Bella", 23, "10-03-2000", 9.8)
print("Methods inherited from Person Base class: ")
sg.display()
print("Methods inherited from Student Base class: ")
sg.displayInfo()
print("Methods inherited from child class: ")
sg.display_student_grade()
