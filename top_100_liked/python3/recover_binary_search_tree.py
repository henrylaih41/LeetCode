# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.found = None
        self.next = None
        self.prev = None
        self.last_equal = None
        self.done = 0
        self.inorder(root)
        if(not self.done):
            if(self.last_equal == None):
                self.last_equal = self.next
            self.last_equal.val, self.found.val = self.found.val, self.last_equal.val
        """
        Do not return anything, modify root in-place instead.
        """
    
    def inorder(self, root):
        if(root == None):
            return
        self.inorder(root.left)
        ###
        if(not self.found):
            if(self.prev and self.prev.val > root.val):
                self.found = self.prev
                self.next = root
        else:
            if(not self.last_equal and self.next and self.next.val != root.val):
                self.last_equal = self.prev
            if(self.prev.val > root.val):
                self.done = 1
                self.found.val, root.val = root.val, self.found.val
        self.prev = root
        ###
        self.inorder(root.right)
