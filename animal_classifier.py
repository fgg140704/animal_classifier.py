class Animal:
    def __init__(self, species, has_fur, is_carnivore, num_legs):
        self.species = species
        self.has_fur = has_fur
        self.is_carnivore = is_carnivore
        self.num_legs = num_legs

    def describe(self):
        print(f"This animal is a {self.species}.")
        if self.has_fur:
            print("It has fur.")
        else:
            print("It does not have fur.")
        if self.is_carnivore:
            print("It is a carnivore.")
        else:
            print("It is not a carnivore.")
        print(f"It has {self.num_legs} legs.")

class AnimalClassifier:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def classify(self):
        for animal in self.animals:
            if animal.has_fur:
                if animal.num_legs == 4:
                    if animal.is_carnivore:
                        print(f"The {animal.species} is a mammal.")
                    else:
                        print(f"The {animal.species} is probably a herbivore.")
                else:
                    print(f"The {animal.species} is probably a spider or insect.")
            else:
                if animal.num_legs == 6 or animal.num_legs == 8:
                    print(f"The {animal.species} is probably an arthropod.")
                else:
                    print(f"The {
