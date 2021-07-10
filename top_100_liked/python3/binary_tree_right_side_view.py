# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        
        if(root):
            result.append(root.val)
            self.dfs(root.right, 1, result)
            self.dfs(root.left, 1, result)
        
        return result
    def dfs(self, root, depth, result):
        if(root == None):
            return
        if(depth > self.max_depth):
            result.append(root.val)
            self.max_depth = depth
        self.dfs(root.right, depth+1, result)
        self.dfs(root.left, depth+1, result)
        
