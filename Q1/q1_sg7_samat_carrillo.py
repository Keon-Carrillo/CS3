'''
Keon P. Carrillo
9-Samat
09/24/2026
'''

class Glassware:
    def __init__(self, glasswareType):
        self.glasswareType = glasswareType

class Beaker1(Glassware):
    def __init__(self, glasswareType):
        super().__init__(glasswareType)
        print(glasswareType, "1 has arrived")
    def __del__(self):
        print(self.glasswareType, "1 has shattered")

class Beaker2(Glassware):
    def __init__(self, glasswareType):
        super().__init__(glasswareType)
        print(glasswareType, "2 has arrived")
    def __del__(self):
        print(self.glasswareType, "2 has shattered")

class Beaker3(Glassware):
    def __init__(self, glasswareType):
        super().__init__(glasswareType)
        print(glasswareType, "3 has arrived")
    def __del__(self):
        print(self.glasswareType, "3 has shattered")

class Beaker4(Glassware):
    def __init__(self, glasswareType):
        super().__init__(glasswareType)
        print(glasswareType, "4 has arrived")
    def __del__(self):
        print(self.glasswareType, "4 has shattered")

class Beaker5(Glassware):
    def __init__(self, glasswareType):
        super().__init__(glasswareType)
        print(glasswareType, "5 has arrived")
    def __del__(self):
        print(self.glasswareType, "5 has shattered")

class Tray:
    def __init__(self):
        print("Tray has been made")
        self.beaker1 = Beaker1("Beaker")
        self.beaker2 = Beaker2("Beaker")
        self.beaker3 = Beaker3("Beaker")
        self.beaker4 = Beaker4("Beaker")
        self.beaker5 = Beaker5("Beaker")
    def holdTray(self):
        print("Holding a tray that has 5 beakers")
    def __del__(self):
        del self.beaker1
        del self.beaker2
        del self.beaker3
        del self.beaker4
        del self.beaker5
        print("Tray is gone and the beakers have been destroyed")

tray = Tray()
tray.holdTray()
del tray