# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        ### v1
        targets = set([n.val for n in nodes])
        self.result = None
        #self.dfs(root, targets, len(nodes))
        self.dfs(root, targets)
        return self.result
    ### v1
    """
    def dfs(self, node, targets, n):
        if(node == None or self.result):
            return 0
        
        l = self.dfs(node.left, targets, n)
        r = self.dfs(node.right, targets, n)
        ### lca is in nodes
        if((l + r) == n-1 and node.val in targets):
            self.result = node
        if(l + r == n and not self.result):
            self.result = node
        
        return l + r + (node.val in targets)
    """
    ### v2
    def dfs(self, node, targets):
        if(node == None):
            return 0
        l = self.dfs(node.left, targets)
        r = self.dfs(node.right, targets)
        if(node.val in targets):
            self.result = node
        if(l and r):
            self.result = node
            
        return l or r or (node.val in targets)
        
