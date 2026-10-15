# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(node, low, high):
            if not node:
                return True

            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False

            if node.left:
                leftval = node.left.val < node.val
                if not leftval:
                    return False

            if node.right:
                rightval = node.right.val > node.val
                if not rightval:
                    return False

            return (
                check(node.left, low, node.val)
                and check(node.right, node.val, high)
            )

        return check(root, None, None)