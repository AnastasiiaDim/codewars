def count_smileys(face_list):
    total = 0
    for face in face_list:
        match list(face):
            case [eyes, mouth] if eyes in ":;" and mouth in ")D":
                total += 1
            case [eyes, nose, mouth] if eyes in ":;" and nose in "-~" and mouth in ")D":
                total += 1
    return total

#_______________________________________
# A RegEx, or Regular Expression, is a sequence of
# characters that forms a search pattern.

# RegEx can be used to check if a string
# contains the specified search pattern.
#_______________________________________
# import re
#
# def count_smileys(arr):
#     # Pattern: eyes [:;], optional nose [-~]? <--, mouth [)D]
#     pattern = r"[:;][-~]?[)D]" #r"" - raw string
#
#     count = 0
#     for face in arr:
#         # re.fullmatch checks if whole string fits the pattern
#         if re.fullmatch(pattern, face):
#             count += 1
#     return count