def array_intersect(nums1, nums2):
    dict1 = {}
    dict2 = {}
    rax = []
    for num in nums1:
        dict1[num] = dict1.get(num, 0) + 1
    for num in nums2:
        dict2[num] = dict2.get(num, 0) + 1
    print("dict1: {}".format(dict1))
    print("dict2: {}".format(dict2))
    if len(dict1) > len(dict2):
        dict1, dict2 = dict2, dict1
    for key, value in dict1.items():
        if key in dict2:
            frequency = dict1[key] if dict1[key] < dict2[key] else dict2[key]
            print("key: {}, freq: {}".format(key, frequency))
            rax += [key] * frequency
    return rax

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(array_intersect(nums1, nums2))
