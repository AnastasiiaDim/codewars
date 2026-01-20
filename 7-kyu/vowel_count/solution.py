def get_count(sentence):
    vowels = 0

    for char in sentence:
        if char in "aeiou":
            vowels += 1

    return vowels