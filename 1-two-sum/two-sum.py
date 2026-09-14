class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen.keys():
                return [i, seen[diff]]
            seen[num] = i
        return []
