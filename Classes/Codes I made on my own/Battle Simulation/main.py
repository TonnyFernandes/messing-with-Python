from characters import *

print("\n")
turn = 1
print("The battle begun")
while True:
    # Shows the turn
    print(f"Turn {turn}")

    bob.attack(steve)
    if steve.current_hp <= 0:
        print(f"{bob.name} won with {bob.current_hp} hp remaining")
        break

    steve.attack(bob)
    if bob.current_hp <= 0:
        print(f"{steve.name} won with {steve.current_hp} hp remaining")
        break
    
    turn += 1
    input('Press enter to continue the battle')
    print("\n")

print("The battle has ended")
