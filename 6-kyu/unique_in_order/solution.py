def unique_in_order(sequence):
    result = []

    for element in sequence:
        if not result or element != result[-1]:
            result.append(element)
    return result