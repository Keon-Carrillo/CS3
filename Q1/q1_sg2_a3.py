'''
Keon P. Carrillo
9-Samat
'''
#Establishes the baseline year
baseYear = 1900
#Input
birthYear = int(input("Enter your birth year: "))

#Zodiac sign assignment: Each sign belongs to a range of years and the program will see where your birth year falls into
if 1900 <= birthYear <= 1912:
    print("Your Chinese zodiac sign is: Rat (鼠 / Shǔ)")

elif 1912 < birthYear <= 1924:
    print("Your Chinese zodiac sign is: Ox (牛 / Niú)")

elif 1924 < birthYear <= 1936:
    print("Your Chinese zodiac sign is: Tiger (虎 / Hǔ)")

elif 1936 < birthYear <= 1948:
    print("Your Chinese zodiac sign is: Rabbit (兔 / Tù)")

elif 1948 < birthYear <= 1960:
    print("Your Chinese zodiac sign is: Dragon (龙 / Lóng)")

elif 1960 < birthYear <= 1972:
    print("Your Chinese zodiac sign is: Snake (蛇 / Shé)")

elif 1972 < birthYear <= 1984:
    print("Your Chinese zodiac sign is: Horse (马 / Mǎ)")

elif 1984 < birthYear <= 1996:
    print("Your Chinese zodiac sign is: Goat (羊 / Yáng)")

elif 1996 < birthYear <= 2008:
    print("Your Chinese zodiac sign is: Monkey (猴 / Hóu)")

elif 2008 < birthYear <= 2020:
    print("Your Chinese zodiac sign is: Rooster (鸡 / Jī)")

elif 2020 < birthYear <= 2032:
    print("Your Chinese zodiac sign is: Dog (狗 / Gǒu)")

elif 2032 < birthYear <= 2044:
    print("Your Chinese zodiac sign is:  Pig (猪 / Zhū)")
