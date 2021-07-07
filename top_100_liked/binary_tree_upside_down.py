# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if(root == None):
            return None
        new_root = root
        while(new_root.left):
            new_root = new_root.left
        ### perform the upside down operation from the bottom level
        self.level_nodes = []
        self.dfs(root, 0)
        for levels in reversed(self.level_nodes):
            for node in levels:
                self.upsideDown(node)
                
        return new_root
    ### the node.right should not have children
    def upsideDown(self, node):
        ### 0 child case
        if(node.left == None):
            return
        left = node.left
        right = node.right
        node.left, node.right = None, None
        left.left = right
        left.right = node
        
        
    def dfs(self, root, level):
        if(root == None):
            return
