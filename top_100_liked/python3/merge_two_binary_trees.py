# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if(not root1 and not root2):
            return None
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        l1, r1 = (root1.left, root1.right) if root1 else (None, None)
        l2, r2 = (root2.left, root2.right) if root2 else (None, None)
        root = TreeNode(val1+val2)
        if(l1 or l2):
            root.left = self.mergeTrees(l1, l2)
        if(r1 or r2):
            root.right = self.mergeTrees(r1, r2)
        
        return root
​
