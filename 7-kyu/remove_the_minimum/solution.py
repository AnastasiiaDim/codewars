def remove_smallest(numbers):
    if not numbers:
        return []

    res = numbers.copy()
    smallest = min(res)
    smallest_index = res.index(smallest)
    res.pop(smallest_index)

    return res

# res = numbers.copy()
# res.remove(min(res))