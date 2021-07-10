# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None):
            return None
        prev = None
        while(head.next != None):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        return head
