from characters import Hero, Enemy
from weapons import iron_sword, short_bow

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

print(hero)
print(enemy)
print('')

while True:

    hero.attack(enemy)
    if enemy.health == 0:
        print(f'{hero.name} won with {hero.health} health remaining')
        break

    enemy.attack(hero)
    if hero.health == 0:
        print(f'{enemy.name} won with {enemy.health} health remaining')
        break

    print('')
print('The battle has ended')
input('')