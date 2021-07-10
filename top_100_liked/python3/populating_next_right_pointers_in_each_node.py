"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(root == None):
            return None
        if(root.left == None):
            return root
        self.connect(root.left)
        self.connect(root.right)
        
        root.left.next = root.right
        l, r = root.left, root.right
        while(l.right != None):
            l = l.right
            r = r.left 
            l.next = r
        
        return root
