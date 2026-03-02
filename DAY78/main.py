########### SINGLE INHERITANCE ############

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("some sound")

# Quick Quiz using the "Animal Class"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    def make_sound(self):
        print("Meow")
    def like(self):
        print("I like cats")

c = Cat("Whiskers", "Siamese")
c.make_sound()
c.like()                 
a = Animal("Buddy", "Dog")
a.make_sound()  
