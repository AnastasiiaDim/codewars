def sort_by_length(arr):
    return sorted(arr, key = len)

# Use sorted() with key=len to create a new list ordered by string length.
# The 'key' parameter tells Python to compare the results of len(string)
# instead of comparing the strings alphabetically.