# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if(k == 1):
            return head
        dummy_head = ListNode(0, head)
        prev = dummy_head
        while(head):
            last, head, old_head = self.reverse(head, k)
            prev.next = last
            prev = old_head
        return dummy_head.next
     
    
    def reverse(self, head, k):
        count = 0
        node, nxt = head, head.next
        while(nxt):
            nnxt = nxt.next
            nxt.next = node
            node = nxt
            nxt = nnxt
            count += 1
            if(count == k-1):
                head.next = nxt
                return node, nxt, head
        ### reverse every thing
        if(node == head):
            return head, None, None
        nxt = node.next
        node.next = None
        while(node != head):
            nnxt = nxt.next
            nxt.next = node
            node = nxt
            nxt = nnxt
                    
        return head, None, None
