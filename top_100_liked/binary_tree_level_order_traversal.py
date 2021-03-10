# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.recur(root, 0, result)
        return result
    
    def recur(self, root, depth, result):
        if(root == None):
            return
        if(depth == len(result)):
            result.append([root.val])
        else:
            result[depth].append(root.val)
        self.recur(root.left, depth+1, result)
        self.recur(root.right, depth+1, result)
            
