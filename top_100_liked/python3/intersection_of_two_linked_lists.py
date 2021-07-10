# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b, l, s, r = headA, headB, None, None, None
        while(a.next != None and b.next != None):
            a = a.next
            b = b.next
        
        if(b.next):
            l, s, r = headB, headA, b
        else:
            l, s, r = headA, headB, a
        
        while(r.next != None):
            l = l.next
            r = r.next
        
        while(l != s):
            l = l.next
            s = s.next
            
        return l
        
        
            
        
        
