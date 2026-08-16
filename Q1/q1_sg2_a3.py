'''
Keon P. Carrillo
9-Samat
'''
#Establishes the starting year
baseYear = 1900

#Input
birthYear = int(input("Enter your birth year: "))

#Validation
if birthYear < 1900:
    print("Invalid input. Enter a birth year on or after 1900.")

else:
    #Determines how many years have passed from 1900, up to your birth year
    yearsPassed = (birthYear - 1900)

    #Modolus uses division to check how many times the zodiacs (12) have been fully cycled and grabs the remainder to determine your birth year's place
    if yearsPassed % 12 == 1:
        print("Your Chinese zodiac sign is: Rat (鼠 / Shǔ)")

    elif yearsPassed % 12 == 2:
        print("Your Chinese zodiac sign is: Ox (牛 / Niú)")

    elif yearsPassed % 12 == 3:
        print("Your Chinese zodiac sign is: Tiger (虎 / Hǔ)")

    elif yearsPassed % 12 == 4:
        print("Your Chinese zodiac sign is: Rabbit (兔 / Tù)")

    elif yearsPassed % 12 == 5:
        print("Your Chinese zodiac sign is: Dragon (龙 / Lóng)")

    elif yearsPassed % 12 == 6:
        print("Your Chinese zodiac sign is: Snake (蛇 / Shé)")

    elif yearsPassed % 12 == 7:
        print("Your Chinese zodiac sign is: Horse (马 / Mǎ)")

    elif yearsPassed % 12 == 8:
        print("Your Chinese zodiac sign is: Goat (羊 / Yáng)")

    elif yearsPassed % 12 == 9:
        print("Your Chinese zodiac sign is: Monkey (猴 / Hóu)")

    elif yearsPassed % 12 == 10:
        print("Your Chinese zodiac sign is: Rooster (鸡 / Jī)")

    elif yearsPassed % 12 == 11:
        print("Your Chinese zodiac sign is: Dog (狗 / Gǒu)")

    elif yearsPassed % 12 == 0:
        print("Your Chinese zodiac sign is: Pig (猪 / Zhū)")
