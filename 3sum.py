def threesum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        two_sum = nums[i] * -1
        s, e = i + 1, len(nums) - 1
        while s < e:
            if nums[s] + nums[e] == two_sum:
                result.append([nums[i], nums[s], nums[e]])
                s += 1
                e -= 1
                while s < e and nums[s] == nums[s-1]:
                    s += 1
                while s < e and nums[e] == nums[e+1]:
                    e -= 1
            elif nums[s] + nums[e] > two_sum:
                e -= 1
            else:
                s += 1
    return result

nums = [-1,0,1,2,-1,-4]
print(threesum(nums))
