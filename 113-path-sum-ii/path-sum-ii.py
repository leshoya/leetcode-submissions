# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, targetSum, [], result)
        return result



    def dfs(self, node, targetSum, currentPath, result):
        if not node:
            return
        currentPath.append(node.val)
        if not node.left and not node.right:
            if sum(currentPath) == targetSum:
                result.append(currentPath[:])
        
        self.dfs(node.left, targetSum, currentPath, result)
        self.dfs(node.right, targetSum, currentPath, result)

        currentPath.pop()
