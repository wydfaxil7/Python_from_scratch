############## OBJECT ORIENTED PROGRAMMING ##############

# CLASSES

class person:
    name = "Fazil"
    age= 20
    occupation = "student"
    def info(self): #self is a reference to the current instance of the class
        print(f"{self.name} is a {self.occupation} and is {self.age} years old.")

a = person()
print(a.name)

b=person()
b.name = "ali"
b.age = 25
b.occupation = "engineer"

b.info()