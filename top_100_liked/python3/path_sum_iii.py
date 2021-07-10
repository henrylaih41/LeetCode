# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
        self.count = 0
        
    def pathSum(self, root: TreeNode, summ: int) -> int:
        self.prefix(root, 0, summ)
        return self.count
    def prefix(self, root, summ, target):
        if(root == None):
            return
        summ += root.val
        if(summ == target):
            self.count += 1
        if((summ - target) in self.d):
            self.count += self.d[summ-target]
        if(summ not in self.d):
            self.d[summ] = 1
        else:
            self.d[summ] += 1
        self.prefix(root.left, summ, target)
        self.prefix(root.right, summ, target)
        self.d[summ] -= 1
        
        
    def DPpathSum(self, root, summ):
        """
        self.dp = {}
        fs, nfs = self.recur(root, summ)
        return fs + nfs
        """
    ### too slow
    def recur(self, root, target):
