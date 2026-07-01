class Herbivore:
    def __init__(self):
        self.food_type="plants"
    def eat_plants(self):
        print("eats plants and grass")
class carnivore:
    def __init__(self):
        self.food_type="plants"
    def eat_meat(self):
        print(" eats meat and hunts animals")
class omnivore:
    def __init__(self):
        self.food_type="plants and meat"
    def eat_both(self):
        print("eats both plants and meat")
class bear(Herbivore,carnivore,omnivore):
    def __init__(self,name):
        self.name=name
        Herbivore.__init__(self)
        carnivore.__init__(self)
        omnivore.__init__(self)
    def display(self):
        print(f"{self.name} is a Bear.")
        print("It can:")
        self.eat_plants()
        self.eat_meat()
        self.eat_both()
b=bear("brown bear")
b.display()

