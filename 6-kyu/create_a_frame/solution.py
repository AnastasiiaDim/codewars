def frame(text, char):
    max_width = max(len(word) for word in text)

    horizontal = char * (max_width + 4)
    res = []
    res.append(horizontal)

    for word in text:
        padded_word = word.ljust(max_width)
        res.append(char + " " + padded_word + " " + char)

    res.append(horizontal)
    return "\n".join(res)