def likes(names):
    match names:
        case []: return "no one likes this"
        case [a]: return f"{a} likes this"
        case [a, b]: return f"{a} and {b} like this"
        case [a, b, c]: return f"{a}, {b} and {c} like this"
        case [a, b, *rest]: return f"{a}, {b} and {len(rest)} others like this"

# def likes(names):
#     n = len(names)
#     if n == 0:
#         return "no one likes this"
#     elif n == 1:
#         return f"{names[0]} likes this"
#     elif n == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif n == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         other_counts = n - 2
#         return f"{names[0]}, {names[1]} and {other_counts} others like this"

