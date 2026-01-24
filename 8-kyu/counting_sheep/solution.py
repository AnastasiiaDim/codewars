def count_sheeps(sheep):
    found = 0
    for i in sheep:
        if i == True:
            found += 1

    return found

# def count_sheeps(sheep):
#     return sheep.count(True)