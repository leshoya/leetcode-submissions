class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        length = len(merged)
        if length % 2 == 1:
            return merged[length//2]
        return (merged[length//2 -1] + merged[length//2]) /2