############ MULTILEVEL INHERITANCE ############

class Animal: #BASE CLASS
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def showdetails(self): 
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Cat(Animal): # Derivedclass#1 using base class "Animal"
    def __init__(self, name, breed):
        super().__init__(name, "CAT")
        self.breed = breed
    
    def showdetails(self):
        super().showdetails()
        print(f"Breed: {self.breed}")

class PersianCat(Cat): # Derivedclass#2 using derivedclass#1 "Cat"
    def __init__(self, name, color):
        super().__init__(name, "Persian")
        self.color = color
    
    def showdetails(self):
        super().showdetails()
        print(f"Color: {self.color}")

p = PersianCat("Hazel", "Coal")
p.showdetails()