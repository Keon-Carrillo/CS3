#Multiple Inheritance
class Father:
    eyes = "blue eues"

class Mother:
    hair = "black hair"

class You(Father, Mother):
    def describeYourself(self):
        print("I have", self.eyes, "and", self.hair)

me = You()
me.describeYourself()
