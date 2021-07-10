# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        s = [] # all nodes in stack waiting to go right 
        while(root):
            s.append(root)
            result.append(root.val)
            root = root.left
            
        while(len(s)):
            node = s.pop().right
            while(node):
                s.append(node)
                result.append(node.val)
                node = node.left
        
        return result
            
        
