#anything private is inside the class
#anything public can be accessed outside the class
#anything protected can be passed to a child

class Human:
    name = ""
    age = 15
    __credit_card = "4539 7894 2345"
    def eat():
        print("nom nom nom")
    def sleep():
        print("Zzzzz")

hooman = Human()
hooman.name = "Sir JM"
hooman.age = 33
print(hooman.name, "is", hooman.age, "years old")
print("CC number is", hooman.credit_card)
