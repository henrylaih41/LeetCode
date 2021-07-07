# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = head.next
        head.next = None 
        while(node):
            nxt = node.next
            head = self.insert(head, node)
            node = nxt
            
        return head
    def insert(self, head, target):
        prev = None
        node = head
        ### o->o->(x)o->
        while(node and target.val >= node.val):
            prev = node
            node = node.next
        ### node == None
        if(prev != None):    
            prev.next = target
        else:
            head = target
        target.next = node
        return head
            
