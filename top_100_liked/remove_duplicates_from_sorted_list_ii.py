# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = head
        head = ListNode()
        dummy = head
        while(tail):
            if(tail.next == None or tail.val != tail.next.val):
                head.next = tail
                head = tail
                tail = tail.next
            else:
                val = tail.val
                while(tail and tail.val == val):
                    tail = tail.next
        head.next = None
        return dummy.next
