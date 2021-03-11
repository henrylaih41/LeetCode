# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(len(preorder) == 0):
            return None
        root, pos = TreeNode(val=preorder[0]), inorder.index(preorder[0])
        left_inorder   = inorder[:pos]
        right_inorder  = [] if pos == len(inorder)-1  else inorder[pos+1:]
        left_preorder  = preorder[1:1+len(left_inorder)]
        right_preorder = [] if pos == len(inorder)-1 else preorder[1+len(left_inorder):]
        root.left  = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
