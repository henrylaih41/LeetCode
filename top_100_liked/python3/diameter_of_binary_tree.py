# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxx = -math.inf
        self.dfs(root)
        return self.maxx - 1
    def dfs(self, root):
        if(root == None):
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.maxx = max(self.maxx, l+r+1)
        return max(l, r) + 1
