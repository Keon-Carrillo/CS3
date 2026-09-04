'''
Keon P. Carrillo
9-Samat
09/04/2026
'''

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp = self.hp-amount

arthur = Hero("Arthur", 100)
arthur.take_damage(10)
morgana = Hero("Morgana", 100)

print(f"Arthur's HP: {arthur.hp}")
print(f"Morgana's HP: {morgana.hp}")

        