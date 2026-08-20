# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            currentDiameter = leftDepth + rightDepth
            self.diameter = max(self.diameter, currentDiameter)
            return 1 + max(leftDepth, rightDepth)
        dfs(root)
        return self.diameter