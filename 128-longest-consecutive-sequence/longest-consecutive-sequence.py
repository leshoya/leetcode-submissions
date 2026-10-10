class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nset = set(nums)
        longest = 0

        for n in nset:                    # change nums -> nset
            if n - 1 not in nset:         # add this
                length = 1
                while n + length in nset: # change nums -> nset
                    length += 1
                longest = max(length, longest)

        return longest