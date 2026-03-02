############ SUPER METHOD ############

class A:
    def parent_method(self):
        print("This is class parent A")

class B(A):
    def parent_method(self):
        print("FAZIL")
        super().parent_method()
    def child_method(self):
        print("This is class child B")
        super().parent_method()

# e = B()
# e.child_method()
# e.parent_method()
        
# same thing can be dont with a constructor

class Employee: 
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lag = lang

Ali = Employee("Ali", "123")
Fazil = Programmer("Fazil", "12223", "python")

print(Ali.name)
print(Ali.id)
print(Fazil.name)
print(Fazil.id)
print(Fazil.lag)