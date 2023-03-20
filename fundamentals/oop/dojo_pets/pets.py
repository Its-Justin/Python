class Pet():
    def __init__(self, name, type, tricks, health=0, energy=0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def pet_display_info(self):             # pet_display_info() - will display all pf the pet information 
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Trick: {self.tricks}")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        return self

    def sleep(self):                        # sleep() - increases the pets energy by 25
        sleeping = 25
        self.energy += sleeping
        print("Energy increased by 25.")
        return self

    def eat(self):                          # eat() - increases the pet's energy by 5 & health by 10
        increase_energy = 5
        increase_health = 10
        self.energy += increase_energy
        self.health += increase_health
        print("Health increased 10.")
        print("Energy increased 5.")
        return self

    def play(self):                         # play() - increases the pet's health by 5
        increase_health = 5
        self.health += increase_health
        print("Health increased by 5.")
        return self

    def noise(self):                        # noise() - prints out the pet's sound
        if self.type == "dog":
            print(f"{self.name} said WOOF!") # adding if statements for the type of pet the Ninja has
        elif self.type == "cat":
            print(f"{self.name} said meow.")
        return self


