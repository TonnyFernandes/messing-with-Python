class Weapon:
    def __init__(self, name: str, type: str, damage: int, value: int):
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value
    
    def __str__(self):
        return f'{self.name}'

iron_sword = Weapon(name="Iron Sword",
                    type="Sword",
                    damage=5,
                    value=10)
short_bow = Weapon(name="Short Bow",
                   type="Bow",
                   damage=4,
                   value=8)
fists = Weapon(name="Fists",
               type="Blunt",
               damage=2,
               value=0)
BFG = Weapon(name="B.F.G.",
            type="Plasma Weapon",
            damage=1000,
            value=2000)