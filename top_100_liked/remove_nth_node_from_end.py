from typing import *
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        neighbors = []
        tail = head
        prev = None
        while(tail != None):
            neighbors.append((prev, tail.next))
            prev = tail
            tail = tail.next

        prev, nxt = neighbors[-n]
        if(prev == None and nxt == None):
            return None
        if(prev == None):
            return nxt
        elif(nxt == None):
            prev.next = None
            return head
        else:
            prev.next = nxt
            return head
