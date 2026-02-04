def accum(s):
    result = []
    for i, char in enumerate(s): # enumerate allows you to loop through an iterable, gives index and num at the same time
        part = char * (i + 1)
        result.append(part.capitalize())
    return "-".join(result)

#for i, char in enumerate("abcd", start=1):
    print(char * i) # prints a, bb, ccc, dddd

