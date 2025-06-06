from random import randint as rd

class Weapon:
    def __init__(self,
                name: str,
                min_damage: int,
                max_damage: int,
                id: int,
                drawback: int
                ) -> None:
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.id = id
        self.drawback = drawback
    
    @property
    def damage(self):
        return rd(self.min_damage, self.max_damage)

wooden_bow = Weapon(name="Wooden Bow", min_damage=5, max_damage=5, id=1, drawback=0)
iron_sword = Weapon(name="Iron Sword", min_damage=0, max_damage=8, id=2,drawback=0)