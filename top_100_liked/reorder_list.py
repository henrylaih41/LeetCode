# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        nxt = slow.next 
        slow.next = None
        ### nxt is now the mid or mid + 1 node
        last = self.reverse(nxt)
        ### if even head->o->o->o->none none<-o<-o<-o<-last
        ### if old head->o->o->none none<-o<-o
        ### last would reach None first (in odd case)
        tail = dummy
        
        while(last):
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = last
            last = last.next
            tail = tail.next
            
        if(head):
            tail.next = head
            tail = tail.next
        return dummy.next
            
    def reverse(self, head):
        prev = None ### this should not be in while loop
        while(head):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
