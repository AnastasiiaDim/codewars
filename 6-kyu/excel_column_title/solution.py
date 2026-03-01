def get_column_title(num):
    if not isinstance(num, int):  # if type(num) is not int:
        raise TypeError("Argument must be an integer")
    if num < 1:
        raise IndexError("Index must be greater than 0")

    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while num > 0:
        num -= 1
        index = num % 26
        result.append(alphabet[index])
        num //= 26

    return "".join(reversed(result))

print(get_column_title(432778)) # Easter Egg :)