# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.getDiff(root, target)
    
    ### O(logn)
    def getDiff(self, root, value):
        diff, n = math.inf, None
        while(root):
            if(abs(value-root.val) < diff):
                diff, n = abs(value-root.val), root.val
            if(root.val == value):
                return root.val
            elif(root.val > value):
                root = root.left
            else:
                root = root.right
        return n
