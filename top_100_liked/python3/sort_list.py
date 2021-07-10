# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
### merge sort on link list?
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)
        
    
    def mergeSort(self, head):
        if(head == None or head.next == None):
            return head
        half = self.findHalf(head)
        h1 = self.mergeSort(head)
        h2 = self.mergeSort(half)
        return self.mergeTwoLists(h1, h2)
        
 
        
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        ans = head
        while(l1 and l2):
            if(l1.val < l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            
        while(l1):
            head.next = l1
            head = head.next
            l1 = l1.next
        while(l2):
            head.next = l2
            head = head.next
            l2 = l2.next
            
        return ans.next
    
    def findMax(self, head):
        maxx = 0
        while(head != None):
