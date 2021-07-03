# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyhead = ListNode(0, head)
        cur, p = dummyhead, dummyhead
        nxt = cur.next
        while(nxt):
            if(nxt.val < x):
                p, cur = self.insert(cur, p)
                nxt = cur.next
            else:
                cur = nxt
                nxt = nxt.next
                
        return dummyhead.next
    
    def insert(self, cur, p): # insert instead of swap
        if(cur == p):
            return cur.next, cur.next
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = p.next
        p.next = nxt
        return nxt, cur
