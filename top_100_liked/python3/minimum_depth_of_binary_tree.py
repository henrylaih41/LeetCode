import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### bfs
    def minDepth(self, root):
        if(root == None):
            return 0
        s = collections.deque([(root, 1)])
        while(len(s)):
            n, d = s.popleft()
            if(not n.left and not n.right):
                return d
            if(n.left):
                s.append((n.left, d+1))
            if(n.right):
                s.append((n.right, d+1))
    
    ### dfs
    def v1minDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        self.minn = math.inf
        self.recur(root, 1)
        return self.minn 
    def recur(self, root, depth):
        if(self.minn <= depth):
            return
        
        if(root.left):
            self.recur(root.left, depth+1)
