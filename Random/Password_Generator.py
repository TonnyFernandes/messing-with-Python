from random import choice, randint
import string

def password_generator() -> str:
    # # # CONSTANTS # # #
    LOWER = list(string.ascii_lowercase)
    UPPER = list(string.ascii_uppercase)
    NUMBER = list('0123456789')
    SYMBOL = list('@#$%&*,.-;:_+')
    BOOL = [True, False]

    # # # Defining possible characters to enter the password, plus its lenght # # #
    HAS_LOWER = choice(BOOL)
    HAS_UPPER = choice(BOOL)
    HAS_NUMBER = choice(BOOL)
    HAS_SYMBOL = choice(BOOL)
    while not HAS_LOWER and not HAS_UPPER and not HAS_NUMBER and not HAS_SYMBOL:
        HAS_LOWER = choice(BOOL)
        HAS_UPPER = choice(BOOL)
        HAS_NUMBER = choice(BOOL)
        HAS_SYMBOL = choice(BOOL)
    PASS_LENGHT = randint(8, 16)

    POSSIBLE_GROUPS = []
    if HAS_LOWER:
        POSSIBLE_GROUPS.append(1)
    if HAS_UPPER:
        POSSIBLE_GROUPS.append(2)
    if HAS_NUMBER:
        POSSIBLE_GROUPS.append(3)
    if HAS_SYMBOL:
        POSSIBLE_GROUPS.append(4)

    # # # Generating the password # # #
    password = ''
    i = 0
    while i < PASS_LENGHT:  
        character = choice(POSSIBLE_GROUPS)
        match(character):
            case 1:
                password += choice(LOWER)
            case 2:
                password += choice(UPPER)
            case 3:
                password += choice(NUMBER)
            case 4:
                password += choice(SYMBOL)
        i += 1
    
    return password

# # # If running this file directly, print a password on the terminal # # #
if __name__ == "__main__":
    print(f"Here's your password: {password_generator()}")