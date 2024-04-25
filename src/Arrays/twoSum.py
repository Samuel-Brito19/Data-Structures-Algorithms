def twoSum(nums, target):
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    for i in range(len(nums)):
        y = target - nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]

print(twoSum([1,3,2,6], 5))