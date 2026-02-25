def parts_sums(ls):
    current_sum = sum(ls)
    result = [current_sum]
    # result = [sum(ls)]
    for num in ls:
        current_sum = current_sum - num
        result.append(current_sum)

    return result