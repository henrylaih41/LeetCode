# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q, self.ans = p, q, None
        self.traverse(root)
        return self.ans
    def traverse(self, root):
        if(root == None):
            return 0
        l, r = self.traverse(root.left), self.traverse(root.right)
        if(l and r):
            self.ans = root
        if(root == self.p or root == self.q):
            if(l or r):
                self.ans = root
        
        return l or r or root == self.p or root == self.q
