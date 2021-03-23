import heapq
class MedianFinder:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh, self.maxh = [], []
        self.size = 0
    def addNum(self, num: int) -> None:
        if(self.size % 2 == 0):
            if(len(self.maxh) == 0 or num > -self.maxh[0]):
                heappush(self.minh, num)
                k = heappop(self.minh)
                heappush(self.maxh, -k)
            else:
                heappush(self.maxh, -num)
        else:
            # when size % 2 == 1 maxh must have at least one element
            if(num < -self.maxh[0]):
                heappush(self.maxh, -num)
                k = -heappop(self.maxh)
                heappush(self.minh, k)
            else:
                heappush(self.minh, num)
        self.size += 1
​
    def findMedian(self) -> float:
        if(self.size % 2 == 0):
            return (self.minh[0] - self.maxh[0])/2
        else:
            return -self.maxh[0]
​
​
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
