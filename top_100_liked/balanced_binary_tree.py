# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBal = True
        self.recur(root)
        return self.isBal
    
    def recur(self, root):
        if(root == None):
            return 0
        h1, h2 = self.recur(root.left), self.recur(root.right)
        if(abs(h1-h2) > 1):
            self.isBal = False
        return max(h1, h2) + 1
