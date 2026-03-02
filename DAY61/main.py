############ Inheritance ############

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def showdetails(self):
        print(f"Name: {self.name}, \nSalary: {self.salary}")


class developer(Employee):
    def showLanguage(self):
        print("Python, Java, C++")

e1 = Employee("Fazil", 50000)
e1.showdetails()

e2 = developer("Ali", 60000)
e2.showdetails()
e2.showLanguage()


######## ACCESS SPECIFIERS ############

# Inpython there are no strict access specifiers like public, private, and protected as in other programming languages. However, we can use naming conventions to indicate the intended level of access for class members.
# by default the members of a class are public

# PRIVATE MEMBERS
print("\n")

class Student:
    def __init__(self, name):
        self.__name = name  # private meember

        def getname(self):
            print(f"The PRIVATE name is {self.__name}")

s1 = Student("Fazil")
# print(s1.__name) # this will give an error because __name is a private member and cannot be accessed outside the class
print(s1._Student__name) # this is called name mangling


# PROTECTED MEMBERS
print("\n")

class Car: 
    def __init__(self, model):
        self._model = model # protected member

        def getmodel(self):
            print(f"The PROTECTED model is {self._model}")

c1 = Car("Honda")
print(c1._model)
# the _model is a protected member and can be accessed outside but it is intended to be used within the class and its subclasses only
# like, it is a convention to show it should not be used oustside the class