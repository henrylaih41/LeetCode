from collections import deque
class MovingAverage:
​
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        self.summ = 0
    def next(self, val: int) -> float:
        self.q.append(val)
        self.summ += val
        if(len(self.q) > self.size):
            self.summ -= self.q.popleft()
        return self.summ / len(self.q)
​
​
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
