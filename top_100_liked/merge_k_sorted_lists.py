# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### self written min heap
class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def left(self, idx):
        return (idx+1)*2 - 1

    def right(self, idx):
        return (idx+1)*2

    def parent(self, idx):
        return max(0, (idx-1)//2)

    def pop(self):
        minn = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1
        self.sink(0)
        return minn

    def insert(self, value, head):
        if(self.size == len(self.arr)):
            self.arr.append([value, head])
        else:
            self.arr[self.size] = [value, head]
        pt = self.size
        self.size += 1
        print(self.arr[pt][0], self.arr[self.parent(pt)][0])
        while(self.arr[pt][0] < self.arr[self.parent(pt)][0]):
            self.swap(pt, self.parent(pt))
            pt = self.parent(pt)

    def sink(self, num):
        minn = num
        l, r = self.left(num), self.right(num)
        if(l < self.size and self.arr[l][0] < self.arr[minn][0]):
            minn = l
        if(r < self.size and self.arr[r][0] < self.arr[minn][0]):
            minn = r
        if(minn != num):
            self.swap(minn, num)
            self.sink(minn)

    def swap(self, a, b):
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_h = MinHeap()
        for head in lists:
            if(head != None):
                min_h.insert(head.val, head)
        ### edge case (all empty)
        if(min_h.size == 0):
            return None
        ans_head = ListNode("dummy")
        ans_tail = ans_head
        # we keep the min_h.size <= k so complexity should be O(klogk)
        # (since lists[i].length <=  500 = O(1))
        while(min_h.size):
            val, head = min_h.pop()
            ans_tail.next = ListNode(val)
            ans_tail = ans_tail.next
            if(head.next != None):
                min_h.insert(head.next.val, head.next)

        return ans_head.next
