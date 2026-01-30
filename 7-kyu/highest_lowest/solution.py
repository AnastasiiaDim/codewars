def high_and_low(numbers):
    nums = [int(n) for n in numbers.split()]
    return f"{max(nums)} {min(nums)}"