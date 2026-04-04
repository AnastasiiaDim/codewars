def parse_int(string):
    words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
        'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
        'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }
    tokens = string.replace('-', ' ').split()

    total = 0
    current_segment = 0

    for token in tokens:
        if token == 'and':
            continue

        value = words[token]

        if value == 100:
            current_segment *= value
        elif value >= 1000:
            current_segment *= value
            total += current_segment
            current_segment = 0
        else:
            current_segment += value

    return total + current_segment