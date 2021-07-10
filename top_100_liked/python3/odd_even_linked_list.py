# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        ehead = head.next
        otail, etail = head, ehead
        while(etail and etail.next):
            otail.next = etail.next
            otail = otail.next
            etail.next = otail.next
            etail = etail.next
        otail.next = ehead
        return head
