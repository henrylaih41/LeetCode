# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.result = []
        self.dfs(root, [])
        return ["->".join(p) for p in self.result]
    
    def dfs(self, node, path):
        if(node == None):
            return
        path.append(str(node.val))
        if(node.left or node.right):
            self.dfs(node.left, path)
            self.dfs(node.right, path)
        else:
            self.result.append(list(path))
        path.pop()
        
