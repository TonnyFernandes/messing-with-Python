def letter_counter(string: str) -> int:
    string.strip()
    string.lower()
    counter = 0
    for char in string:
        if char.isalpha():
            counter += 1
    return counter

def count_letter_on_first_word(string: str) -> int:
    string.strip()
    string.lower()
    counter = 0
    
    return counter

name = input('Type your entire name: ')
print(f'Your name have {letter_counter(name)} letters')