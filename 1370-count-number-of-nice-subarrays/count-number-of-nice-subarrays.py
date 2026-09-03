class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = odd = l = 0

        for r in range(len(nums)):
            odd += nums[r] % 2

            while odd > k:
                odd -= nums[l] % 2
                l += 1

            if odd == k:
                m = l
                while nums[m] % 2 == 0:
                    m += 1
                res += m - l + 1

        return res