# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, [], targetSum)
        return self.result
    
    def dfs(self, root, comb, summ):
        if(root == None):
            return
        ### is leaf
        if(not root.right and not root.left):
            if(summ == root.val):
                comb.append(root.val)
                self.result.append(list(comb))
                comb.pop()
            return
        
        comb.append(root.val)
        self.dfs(root.left, comb, summ-root.val)
        self.dfs(root.right, comb, summ-root.val)
        comb.pop()
        
