# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if(head == None):
            return head
        slow, fast, cnt = head, head, -1
        while(slow.next != None and fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                cnt = self.cycleCount(slow, fast)
                break
        if(cnt == -1):
            return None
        fast = head
        for i in range(cnt):
            fast = fast.next
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow
    
    def cycleCount(self, slow, fast):
        count = 0
        while(slow != fast):
            slow = slow.next
            fast = fast.next.next
            count += 1
        return count
