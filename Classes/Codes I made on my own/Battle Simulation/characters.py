from weapons import *
from armors import *

class Character:
    def __init__(self,
                name: str,
                base_hp: int,
                base_strength: int,
                armor: object,
                weapon: object
                ) -> None:
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.base_strength = base_strength
        self.base_hp = base_hp
        self.current_hp = base_hp + self.armor.hp

    @property
    def strength(self):
        return self.base_strength + self.weapon.damage
    
    def attack(self,
               target: object):
        dmg = self.strength
        target.current_hp -= dmg
        print(f"{self.name} dealt {dmg} damage to {target.name}")
        print(f"{target.name} now have {target.current_hp} remaining hp\n")


class Knight(Character):
    def __init__(self,
                name,
                base_hp,
                base_strength,
                armor=None,
                weapon=None) -> None:
        armor = armor if armor is not None else heavy_armor
        weapon = weapon if weapon is not None else iron_sword
        super().__init__(name=name,
                        base_hp=base_hp,
                        base_strength=base_strength,
                        armor=armor,
                        weapon=weapon
                        )
        

steve = Knight(name="Steve", base_hp=100, base_strength=10)
bob = Knight(name="Bob", base_hp=75, base_strength=15)