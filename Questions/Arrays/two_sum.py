class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in h:
                return [h[y], i]
            h[n] = i
