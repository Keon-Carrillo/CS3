#AGGREGATION
class Sauce:
    def __init__(self,name,taste):
        self.name = name; self.taste = taste
        print(self.name, "is ready")

class Tusoktusok:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        print(self.name, "is cooked and has", self.sauce.name)
    def eat(self):
        print("I am eating", self.name, "and it tastes", self.sauce.taste)
    def __del__(self):
        print(self.name, "was thrown in the trashcan")

hotsauce = Sauce("Hot sauce", "spicy")
fishball = Tusoktusok("fishball", hotsauce)
fishball.eat()
del fishball

print(hotsauce.name)
