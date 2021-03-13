"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head == None):
            return None
        tail, prev = head, None
        while(tail != None):
            new = Node(tail.val, None, tail.random)
            if(prev):
                prev.next = new
            prev = new
            nxt = tail.next
            tail.next = new
            tail = nxt
           
            
        ntail = head.next
        while(ntail != None):
            if(ntail.random != None):
                ntail.random = ntail.random.next
            ntail = ntail.next
        return head.next
            
