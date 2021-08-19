# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while(head and head.val == val):
            head = head.next
        node = head
        while(node and node.next):
            if(node.next.val == val):
                rep = node.next
                while(rep and rep.val == val):
                    rep = rep.next
                node.next = rep
            node = node.next
        return head
