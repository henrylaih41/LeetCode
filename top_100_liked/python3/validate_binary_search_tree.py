import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        v, _, _ = self.recur(root)
        return v
        
    def recur(self, root):
        if(root == None):
            return 1, -math.inf, math.inf
        lv, lmax, lmin = self.recur(root.left)
        rv, rmax, rmin = self.recur(root.right)
        if(not lv or not rv):
            return 0, 0, 0
        minn = min(root.val, lmin, rmin)
        maxx = max(root.val, lmax, rmax)
        valid = (root.val > lmax and root.val < rmin)
        return valid, maxx, minn
