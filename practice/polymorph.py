"""class Animal:
    def sound(self):
        print("Animal sound!!!")

class Dog(Animal):
    def sound(self):
        print("Dog Sound!!!")

class Cat(Animal):
    def sound(self):
        print("Cat sound!!!")

animals=[Dog(),Cat()]

for a in animals:
    a.sound()"""



"""def add(a=0,b=0,c=0):
    return a+b+c

print(add())
"""

"""class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value

n1=Number(10)
n2=Number(20)

print(n1+n2)
"""

class Dog:
    def speak(self):
        print("Bark")
class Human:
    def speak(self):
        print("Hello")
def call(obj):
    obj.speak()

call(Dog())
call(Human())
