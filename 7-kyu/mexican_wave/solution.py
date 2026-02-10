def wave(string):
    result = []

    for index in range(len(string)):
        if string[index] != " ":
            # make them together: before + UPPER + after
            new_word = string[:index] + string[index].upper() + string[index + 1:]
            # [:i] takes everything before the index not including it
            # [i + 1:] takes everything after it
            result.append(new_word)

    return result

# Using list comprehension to create the wave
# .isalpha() ensures we only flip the case for actual letters, ignoring spaces/symbols

# return [string[:index] + string[index].upper() + string[index + 1:] if string[index].isalpha()]
