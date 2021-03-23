# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -1
        self.count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.target = k
        self.inorder(root)
        return self.ans
    
    def inorder(self, root):
        if(self.ans != -1 or root == None):
            return
        self.inorder(root.left)
        self.count += 1
        if(self.count == self.target):
            self.ans = root.val
        self.inorder(root.right)
