def count_smileys(face_list):
    total = 0
    for face in face_list:
        symbols = list(face)
        match symbols:
            case [eyes, mouth] if eyes in ":;" and mouth in ")D":
                total += 1
            case [eyes, nose, mouth] if eyes in ":;" and nose in "-~" and mouth in ")D":
                total += 1
    return total
