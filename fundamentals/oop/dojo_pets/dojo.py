from pets import Pet                       # will link the pets file and Pet class

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet("Buster", "dog", "sit")
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):                       # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self

    def feed(self):                       # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self

    def bathe(self):                      # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self

    def pet_info(self):                   # pet_info() will display all of the pets information in the Pet class
        self.pet.pet_display_info()

person1 = Ninja("Joe", "Doe", "bone", "steak")

person1.feed().walk().bathe()
