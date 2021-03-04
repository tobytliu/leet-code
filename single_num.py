def single_num(nums): # figure out why typing fucks up
    unique_nums = set(nums)
    double_sum = 2 * sum(unique_nums)
    return double_sum - sum(nums)

nums = [1]
print(single_num(nums))
