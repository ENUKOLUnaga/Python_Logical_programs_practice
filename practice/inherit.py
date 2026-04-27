"""class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks=marks
    def display(self):
        print(self.name ,self.marks)

s=Student("Nagendra",90)
s.display()
"""

class A:
    def show(self):
        print("A")

class B(A):
    pass
    #def show(self):
    #    print("B")

class C(A):
    pass
    #def show(self):
    #    print("C")

class D(C,B):
    pass

d=D()

d.show()

print(D.__mro__)