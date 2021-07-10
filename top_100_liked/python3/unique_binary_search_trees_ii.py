from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### bottom up dp
    def generateTrees(self, n: int) -> List[TreeNode]:
        dp = [[] for _ in range(n+1)]
        dp[0].append(None)
        dp[1].append(TreeNode(1))
        for i in range(2, n+1):
            for k in range(i):
                for l_root in dp[k]:
                    for r_root in dp[i-1-k]:
                        new_root = TreeNode(-1)
                        new_root.left, idx = self.copyTree(l_root, 1)
                        new_root.val = idx
                        new_root.right, _ = self.copyTree(r_root, idx+1)
                        dp[i].append(new_root)
        
        #for r in dp[n]:
        #    self.assignNumber(r, 1)
        return dp[n]
        
    def assignNumber(self, root, idx):   
        if(root == None):
            return idx
        idx = self.assignNumber(root.left, idx)
        root.val = idx
        idx = self.assignNumber(root.right, idx+1)
        
        return idx
    
    def copyTree(self, root, idx):
        if(root == None):
            return None, idx
        n = TreeNode(0)
        n.left, idx = self.copyTree(root.left, idx)
        n.val = idx
        n.right, idx = self.copyTree(root.right, idx+1)
        return n, idx
