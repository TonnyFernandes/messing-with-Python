# Definition
#   classes: blueprints for specific objects
#       objects: stuff we impletent using classes
from weapons import fists, short_bow

class Character:
    # If a variable is set here, it will be shared across all objects

    def __init__(self,
                name: str,
                health: int
                ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage

        print(f'{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}')
        print(f'{target.name} now have {target.health} health points')
        # target.health = max(target.health, 0)
            # This don't allow the health going bellow 0, but I won't do it because overkill go brr
    
    def __str__(self):
        return f"{self.name} have {self.health} health points and is using {self.weapon} as a weapon"

class Hero(Character):
    def __init__(self,
                name: str,
                health: int
                ) -> None:
        super().__init__(name=name, health=health)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped {self.weapon.name}\n')

class Enemy(Character):
    def __init__(self,
                name: str,
                health: int,
                weapon
                ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon