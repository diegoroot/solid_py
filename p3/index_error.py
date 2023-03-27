class Animal:

    def __init__(self, name, species):
        self.__name = name
        self.__species = species
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, new_species):
        self.__species = new_species
    
    def walk(self):
        print(self.species + " Camina")
    
    def jump(self):
        print(self.species + " Salta")

def ActionJumpHole(animal: Animal):
    animal.walk()
    animal.jump()
    animal.walk()    


dog = Animal('Dog', 'Canine')
ActionJumpHole(dog)
print()









#Part2
class Animal:

    def __init__(self, name, species):
        self.__name = name
        self.__species = species
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, new_species):
        self.__species = new_species
    
    def walk(self):
        print(self.name + " Camina")
    
    def jump(self):
        print(self.name + " Salta")


class Elephant(Animal):

    def jump(self):
        print(self.name + " No puede saltar")
        raise

def ActionJumpHole(animal: Animal):
    try:
        animal.walk()
        animal.jump()
        animal.walk()
    except Exception as e:    
        print(animal.name + " se cae al hueco")

dog = Animal('Dog', 'Canine')
ActionJumpHole(dog)
print()

elephant = Elephant('Elephant', 'Mammals')
ActionJumpHole(elephant)
