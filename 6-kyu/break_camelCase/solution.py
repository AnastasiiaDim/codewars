def solution(string):
    result = []

    for char in string:
        if char.isupper():
            result.append(" ")
        result.append(char)

    return "".join(result)

# return "".join([" " + char if char.isupper() else char for char in s])

#Ternary Operator
# Syntax: <value_if_true> if <condition> else <value_if_false>
# It's a one-line way to choose between two values based on a condition