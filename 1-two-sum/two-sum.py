class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {} #value, index
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in map:
                return [i, map[diff]]
            map[num] = i
        return []