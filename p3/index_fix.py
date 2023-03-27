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

class LightWeightAnimal(Animal):
    
    def jump(self):
        print(self.species + " Salta")

def ActionJumpHole(animal: LightWeightAnimal):
    animal.walk()
    animal.jump()
    animal.walk()


dog = LightWeightAnimal('Dog', 'Canine')
ActionJumpHole(dog)

elephant = Animal('Elephant', 'Mammals')

fish = Animal('Carpa', 'Fish') # es un animal realmente?