######### CLASS METHODS AS ALTERNATIVE CONSTRUCTORS #########

class Employee:
    company = "Apple"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod # here is used the class method as alternative constructor
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
        
emp1 = Employee("John", 100000)
print(emp1.name, emp1.salary)

string = "Fazil-122000"
emp2 = Employee.fromstr(string)
print(emp2.name, emp2.salary)