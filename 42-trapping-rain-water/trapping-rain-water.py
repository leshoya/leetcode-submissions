class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        for i in height:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1

            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -=1
        return res

        


        