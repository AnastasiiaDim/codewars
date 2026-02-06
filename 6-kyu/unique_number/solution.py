def find_uniq(arr):
    a, b = set(arr)
    if arr.count(a) == 1:
        return a
    else:
        return b

    # return a if arr.count(a) == 1 else b