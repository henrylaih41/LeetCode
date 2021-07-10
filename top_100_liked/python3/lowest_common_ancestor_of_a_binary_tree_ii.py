# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #self.res = None
        #self.v1dfs(root, p, q)
        #return self.res
        self.result = None
        self.dfs(root, p, q)
        return self.result
    def v1dfs(self, node, p, q):
        if(node == None or self.res):
            return 0
        l = self.v1dfs(node.left, p, q)
        r = self.v1dfs(node.right, p, q)
        count = l + r + (node.val == p.val or node.val == q.val)
        if(count == 2 and not self.res):
            self.res = node
        return count
    ### like this one more
    def dfs(self, node, p, q):
        if(not node):
            return node
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right,p, q)
        if(l and r):
            self.result = node
