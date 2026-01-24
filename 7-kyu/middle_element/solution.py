def gimme(input_array):
    sorted_nums = sorted(input_array)
    x = sorted_nums[1]
    return input_array.index(x)

#
# result = gimme([1, 6, 3])
# print(result)

#OR
# return input_array.index(sorted(input_array)[1])

