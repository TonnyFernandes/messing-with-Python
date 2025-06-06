def decimal_to_binary(decimal) -> int:
    # # # Handling invalid inputs and converting into intenger # # #
    if not decimal.isdigit():
        raise ValueError('Input must be a decimal number!')
    decimal = int(decimal)
    if decimal < 0:
        raise ValueError('Input must be a positive decimal number!')
    # # # Handling edge case # # #
    if decimal == 0:
        return 0

    # # # Converting # # #
    binary: list = []
    while decimal > 0:
        binary.append(str(decimal%2))
        decimal //= 2
    
    return int(''.join(reversed(binary)))

d = input('Type a decimal number: ')
print(decimal_to_binary(d))