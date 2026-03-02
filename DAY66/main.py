####### CLASS VARIBALE vs INSTANCE VARIABLE #######

class Employee:
    #class variable
    company_name = "Apple"
    noEmployee = 0

    def __init__(self, name):
        #instance variable
        self.name = name
        self.salary = 100000
        Employee.noEmployee += 1
    
    def showdetails(self):
        print(f"The name of the {self.company_name}'s employee is {self.name} and salary is {self.salary}")
        print(f"Total number of employees in {self.company_name} is {Employee.noEmployee}")    

emp1 = Employee("John")
emp2 = Employee("Fazil")
emp2.showdetails()
emp1.salary = 130000
emp1.company_name = "Microsoft"
Employee.company_name = "Google"
emp1.showdetails()
emp2.showdetails()
