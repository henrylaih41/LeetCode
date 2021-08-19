# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.move = 0
        self.dfs(root)
        return self.move
    
    def dfs(self, root):
        if(root == None):
            return 0, 0
        left_coins, left_nodes = self.dfs(root.left)
        right_coins, right_nodes = self.dfs(root.right)
        self.move += (abs(left_coins - left_nodes) + abs(right_coins - right_nodes))
        return left_coins + right_coins + root.val, left_nodes + right_nodes + 1
        
