# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0, head)
        prev = dummy_head
        while(prev.next and prev.next.next):
            first = prev.next
            prev.next = first.next
            first.next = prev.next.next
            prev.next.next = first
            prev = first
        return dummy_head.next
            
