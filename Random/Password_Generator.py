from random import choice, shuffle
import string

def password_generator(
    PASS_LENGHT: int = 16,
    include_lowercase: bool = True,
    include_uppercase: bool = True,
    include_number: bool = True,
    include_symbol: bool = True
) -> str:
    """Generate a password within the specified rules. The rules have a default state but, when calling the function, it is possible to change them to a certain degree. 

    Args:
        PASS_LENGHT: desired lenght of the password (default: 16)
        include_lowercase: if password include a lowercase character (default: true)
        include_uppercase: if password include a uppercase character (default: true)
        include_number: if password include a number character (default: true)
        include_symbol: if password include a special character (default: true)
    
    Return:
        Generated password
    
    Raises:
        ValueError: If no character list is selected or PASS_LENGHT is lesser than 6
    """
    
    # # # CONSTANTS # # #
    LOWER = list(string.ascii_lowercase) if include_lowercase else []
    UPPER = list(string.ascii_uppercase) if include_uppercase else []
    NUMBER = list(string.digits) if include_number else []
    SYMBOL = list(string.punctuation) if include_symbol else []
    ALL_CHAR = LOWER + UPPER + NUMBER + SYMBOL

    # # # ValueError # # #
    if PASS_LENGHT < 6:
        raise ValueError('Password lenght must be at least 6')
    if not ALL_CHAR:
        raise ValueError('At least one group of characters must be selected')

    # # # Generating the password # # #
    password = []
    i = 0
    # Ensuring one character of each possible list enters the password
    if include_lowercase:
        password.append(choice(LOWER))
        i += 1
    if include_uppercase:
        password.append(choice(UPPER))
        i += 1
    if include_number:
        password.append(choice(NUMBER))
        i += 1
    if include_symbol:
        password.append(choice(SYMBOL))
        i += 1
    # Filling the rest of the password
    while i < PASS_LENGHT:  
        password.append(choice(ALL_CHAR))
        i += 1
    # Shuffling the password to ensure randomness
    shuffle(password)

    return ''.join(password)

# # # If running this file directly, print a password on the terminal # # #
if __name__ == "__main__":
    print(f"Here's your password: {password_generator()}")