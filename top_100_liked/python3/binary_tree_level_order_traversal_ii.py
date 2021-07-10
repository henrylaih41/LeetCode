# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### sorting is O(nlogn)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.dfs(root, 0)
        return reversed(self.result)
    
    def dfs(self, root, level):
        if(root == None):
            return
        
        if(len(self.result) == level):
            self.result.append([])
        
        self.result[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
