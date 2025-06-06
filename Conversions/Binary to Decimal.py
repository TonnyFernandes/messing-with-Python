def binary_to_decimal(binary: str) -> int:
    # # # Handling invalid inputs # # #
    if not all(c in '01' for c in binary):
        raise ValueError('Invalid! Input must be binary!')
    
    # # # Converting # # #
    decimal = 0
    for power, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** power)
    return int(decimal)
    

b = input('Type a binary number: ')
print(binary_to_decimal(b))