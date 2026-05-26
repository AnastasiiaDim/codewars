def pig_it(text):
    result = []
    words = text.split()

    for word in words:
        if word.isalpha():
            first_letter = word[0]
            pig_word = f"{word[1:]}{word[0]}ay"
            result.append(pig_word)
        else:
            result.append(word)

    return " ".join(result)