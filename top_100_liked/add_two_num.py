class Solution:
    def add(self, l1, l2, nxt):
        ss = l1.val + l2.val + nxt
        remain = ss % 10
        nxt    = ss // 10
        return ListNode(remain, None), nxt

    def preprocess(self, l1, l2):
        while(l1.next != None or l2.next != None):
            if(l2.next == None):
                l2.next = ListNode(0, None)
            if(l1.next == None):
                l1.next = ListNode(0, None)
            l1, l2 = l1.next, l2.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # preprocess
        self.preprocess(l1,l2)
        head, nxt = self.add(l1, l2, 0)
        tail = head
        l1, l2 = l1.next, l2.next

        while(l1 != None): # since l1, l2 is guarenteed to has the same size
            tail.next, nxt = self.add(l1, l2, nxt)
            l1, l2 = l1.next, l2.next
            tail = tail.next

        if(nxt > 0): # nxt would not exceed 9
            tail.next = ListNode(nxt, None)

        return head
