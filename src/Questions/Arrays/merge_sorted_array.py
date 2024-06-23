def runningSum(self, nums: list):
    result = []
    for n in range(nums):
        a = nums[n] + nums[n + 1]
        n += 1
    return print(a)


print(runningSum([1, 2, 3, 4]))
