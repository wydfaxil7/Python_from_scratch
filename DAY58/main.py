########## CONSTRUCTORS ###########

class person:
    def __init__(self, n, a ,o): #constructor method, it is called when an instance of the class is created
        self.name = n
        self.age = a
        self.occupation = o
    
    def info(self):
        print(f"{self.name} is a {self.occupation} and is {self.age} years old.")

a = person("Fazil", 20, "Developer")
b = person("Ali", 25, "Engineer")
a.info()
b.info()