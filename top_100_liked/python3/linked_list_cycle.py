# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None):
            return False
        tail, prev = head, None
        while(tail.next != None):
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt
            if(id(tail) == id(head)):
                return True
            
        return False
