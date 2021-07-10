# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.srob = {}
        self.nsrob = {}
        if(root == None):
            return 0
        maxx = max(self.nsmax(root), self.smax(root))
        return maxx
        
    ### maximum money if rob root
    def smax(self, root):
        if(root == None):
            return 0
        if(root in self.srob):
            return self.srob[root]
        maxx = root.val + self.nsmax(root.left) + self.nsmax(root.right)
        self.srob[root] = maxx
        return maxx
        
    ### maximum money if not rob root
    def nsmax(self, root):
        if(root == None):
            return 0
        if(root in self.nsrob):
            return self.nsrob[root]
        
        maxl = max(self.smax(root.left), self.nsmax(root.left))
        maxr = max(self.smax(root.right), self.nsmax(root.right))
        self.nsrob[root] = maxl + maxr
        return maxl + maxr
