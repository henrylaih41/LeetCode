# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = head
        tail = head
        while(head):
            while(tail and tail.val == head.val):
                tail = tail.next
            head.next = tail
            head = tail
        return start
        
