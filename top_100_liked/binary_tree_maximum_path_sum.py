import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxx, _ = self.findMax(root)
        return maxx
    
    def findMax(self, root):
        if(root == None):
            return -math.inf, -math.inf
        lmax, lmaxp = self.findMax(root.left)
        rmax, rmaxp = self.findMax(root.right)
        smax = max(lmaxp, rmaxp, lmaxp+rmaxp, 0) + root.val
        maxx = max(lmax, rmax, smax)
        maxSubPath = max(lmaxp + root.val, rmaxp + root.val, root.val)
        return maxx, maxSubPath
