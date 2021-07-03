# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        ### we can also opt here, use a index to
        ### keep track of the tail of post
        ### if we can modify the pass in arg we can just pop it
        ### post = list(postorder)
        self.mapp = {}
        for i in range(len(inorder)):
            self.mapp[inorder[i]] = i
        return self.recur(inorder, 0, len(inorder)-1, postorder)    
    
    ### O(n^2) complexity becuase inorder.index() is O(n)
    def v1recur(self, inorder, postorder):
        if(len(inorder) == 0):
            return None
        root = TreeNode(postorder.pop())
        i = inorder.index(root.val)
        root.right = self.recur(inorder[i+1:], postorder)
        root.left  = self.recur(inorder[:i], postorder)
        
        return root
    ### O(n) worst time complexity 
    def recur(self, inorder, i, j, postorder):
        if(i > j):
            return None
        root = TreeNode(postorder.pop())
        ### we can optimize here using hashmap
        ### k = inorder.index(root.val)
        k = self.mapp[root.val]
        root.right = self.recur(inorder, k+1, j, postorder)
        root.left  = self.recur(inorder, i, k-1, postorder)
        
        return root
    
​
