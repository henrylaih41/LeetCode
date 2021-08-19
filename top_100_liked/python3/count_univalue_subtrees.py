# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        if(root == None):
            return 0
        self.dfs(root)
        return self.count
        
    ### root is never None, dfs return None if the subtree is 
    ### not uni-value
    def dfs(self, root):
        flag = 0
        if(root.left and root.val != self.dfs(root.left)):
            flag = 1
        if(root.right and root.val != self.dfs(root.right)):
            flag = 1
        if(flag):
            return None
        ### if the code executed here, it means that the subtree of 
        ### root are all uni-value subtree, or they are None
        self.count += 1
        return root.val
            
            
