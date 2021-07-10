# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head == None):
            return head
        count, last = self.count(head)
        k = k % count
        if(k == 0):
            return head
        last.next = head
        step = count - k - 1
        while(step > 0):
            head = head.next
            step -= 1
        return_head = head.next
        head.next = None
        return return_head
        
    
    def count(self, head):
        count = 1
        while(head.next):
            head = head.next
            count += 1
        return count, head
