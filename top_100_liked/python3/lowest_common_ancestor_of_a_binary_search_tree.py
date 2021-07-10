# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if(p.val < q.val):
            p, q = q, p
        while(node):
            if(node.val == p.val or node.val == q.val):
                return node
            if(node.val > q.val and node.val < p.val):
                return node
            elif(node.val < q.val):
                node = node.right 
            else:
                node = node.left
        
