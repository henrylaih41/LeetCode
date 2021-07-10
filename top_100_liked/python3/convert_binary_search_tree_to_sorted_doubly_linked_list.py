"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
​
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = None
        self.prev = None
        self.inorder(root)
        if(self.head == None): # empty tree
            return None
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
    def inorder(self, root):
        if(root == None):
            return
        self.inorder(root.left)
        if(self.head == None):
            self.head = root
        if(self.prev):
            self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.inorder(root.right)
        
