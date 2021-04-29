class NumArray: # BIT (Fenwick Tree)
    def __init__(self, nums):
        self.nums = nums
        self.sums = [0] * (len(nums)+1) # BIT index starts from 1
        self.len = len(nums)
        for i in range(len(nums)):
            self._update(i+1, nums[i])
            
    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update(index+1, delta)
        
    def _update(self, index, delta):     
        while(index <= self.len):
            self.sums[index] += delta
            index += (index & -index)
            
    def sumRange(self, left, right):
        return self._query(right+1) - self._query(left)
    
    def _query(self, index): # the sum of nums[0] ~ nums[index-1]
        summ = 0
        while(index > 0):
            summ += self.sums[index]
            index -= (index & -index)
        return summ
​
class segTreeNode:
    def __init__(self, l, r, val=0, lchild=None, rchild=None):
        self.l, self.r = l, r
        self.sum = val
        self.lchild, self.rchild = lchild, rchild
        
class segTree:
    def __init__(self, nums: List[int]):
        self.root = self.buildNode(0, len(nums)-1)
        for i in range(len(nums)):
            self.update(i, nums[i])
        
    def buildNode(self, l, r):
        s = segTreeNode(l, r)
        if(l == r):
            return s
        mid = (l+r)//2
        s.lchild = self.buildNode(l, mid)
        s.rchild = self.buildNode(mid+1, r)
        return s
​
    def update(self, index: int, val: int) -> None:
        self.treeUpdate(index, val, self.root)
        
    def treeUpdate(self, index, val, node):
        if(node.l == node.r and node.l == index):
            node.sum = val
            return
        mid = (node.l+node.r)//2
