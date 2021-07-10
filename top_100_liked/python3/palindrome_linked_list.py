# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode(-1, head)
        prev = None
        slow, fast = dummy, dummy
        while(fast and fast.next):
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        ### 2k
        if(fast):
            fast = slow.next
            slow.next = prev
        ### 2k+1
        else:
            fast = slow.next
            slow = prev
       
        while(fast and fast.val == slow.val):
            fast = fast.next
            slow = slow.next
        
        if(not fast):
            return True
        
        return False
