def remove_dup(nums):
    nums[:] = list(set(nums))
    return len(nums)

lst = [1, 1, 2]
print(remove_dup(lst))
print(lst)
