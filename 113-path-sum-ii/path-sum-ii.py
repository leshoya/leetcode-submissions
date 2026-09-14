class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.res = []
        self.dfs(root, [], 0)
        return self.res

    def dfs(self, node, path, total):
        if not node:
            return

        total += node.val
        path.append(node.val)
        if not node.left and not node.right:
                if total == self.targetSum:
                    self.res.append(list(path))
        else:
            self.dfs(node.left, path, total)
            self.dfs(node.right, path, total)

        path.pop()