# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sums = 0    
        self.dfs(root, 0)
        return self.sums
    def dfs(self, root, accum_value):
        if(root == None):
            return
        value = accum_value * 10 + root.val
        ### leaf node
        if(root.left == None and root.right == None):
            self.sums += value
            return
        
        self.dfs(root.left, value)
        self.dfs(root.right, value)
