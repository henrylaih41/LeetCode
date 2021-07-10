import collections
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
        head = root
        while(head):
            prev, n = None, head
            head = None
            while(n):
                child = [n.left, n.right]
                for c in child:
                    if(c == None):
                        continue
                    if(head == None):
                        head = c
                    if(prev):
                        prev.next = c
                    prev = c
                n = n.next
        return root
