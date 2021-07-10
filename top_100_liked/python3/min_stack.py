class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack  = []
        self.minn   = math.inf
    
    def push(self, x: int) -> None:
        if(x < self.minn):
            self.stack.append((x, self.minn))
            self.minn = x
        else:
            self.stack.append((x, None))
​
    def pop(self) -> None:
        x, minn = self.stack.pop()
        if(minn):
            self.minn = minn
            
    def top(self) -> int:
        return self.stack[-1][0]
​
    def getMin(self) -> int:
        return self.minn
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
