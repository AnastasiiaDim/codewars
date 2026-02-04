def get_middle(s):
    length = len(s)
    mid = len(s) // 2
    if length % 2 == 0:
        return s[mid -1 : mid + 1]
    else:
        return s[mid]

# return s [ (len(s)-1) //2 : len(s) //2 + 1]
# e.g. s[3:4] returns one symbol [3], s[1:3] returns two symbols [1, 2]