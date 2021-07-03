# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyhead = ListNode(0, head)
        head = dummyhead
        count = 1
        while(count != left):
            head = head.next
            count += 1
        cur = head.next
        nxt = cur.next
        while(count != right):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
            count += 1
        head.next.next = nxt
        head.next = cur
        
        return dummyhead.next
        
