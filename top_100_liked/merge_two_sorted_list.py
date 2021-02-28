from typing import *
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ans = head
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        while(l1 != None):
            head.next = l1
            head = head.next
            l1 = l1.next
        while(l2 != None):
            head.next = l2
            head = head.next
            l2 = l2.next

        return ans.next
