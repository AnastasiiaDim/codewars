def grabscrab(said, possible_words):
    reference = sorted(said)
    return [word for word in possible_words if sorted(word) == reference]

    # reference = sorted(said)
    # matches = []
    # for word in possible_words:
    #     sorted_word = sorted(word)
    #     if sorted_word == reference:
    #         matches.append(word)
    # return matches