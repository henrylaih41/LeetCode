# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxx = 1
        self.dfs(root)
        return self.maxx
        
    ### returns the number of longest Consecutive including itself
    def dfs(self, node):
        if(node == None):
            return 0, math.inf
        
        l, lv = self.dfs(node.left)
        r, rv = self.dfs(node.right)
        maxx = -math.inf
        if(lv == node.val + 1):
            maxx = max(l+1, maxx)
        if(rv == node.val + 1):
            maxx = max(r+1, maxx)
        self.maxx = max(maxx, self.maxx)
        return max(1, maxx), node.val
