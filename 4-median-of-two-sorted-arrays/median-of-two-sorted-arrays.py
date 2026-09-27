class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):          # binary search over the SHORTER array
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2         # A's partition: i is last index on the left
            j = half - i - 2         # B's partition, so left side has `half` elements

            Aleft  = A[i]     if i >= 0          else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A)  else float("inf")
            Bleft  = B[j]     if j >= 0          else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B)  else float("inf")

            if Aleft <= Bright and Bleft <= Aright:      # valid partition
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:     # A's left side too big, shrink it
                r = i - 1
            else:                    # A's left side too small, grow it
                l = i + 1