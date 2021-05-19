class MyQueue:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_s = []
        self.pop_s  = []
​
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_s.append(x)
​
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if(len(self.pop_s) == 0):
            while(len(self.push_s)):
                self.pop_s.append(self.push_s.pop())
        return self.pop_s.pop()
​
    def peek(self) -> int:
        """
        Get the front element.
        """
        if(len(self.pop_s) == 0):
            while(len(self.push_s)):
                self.pop_s.append(self.push_s.pop())
        return self.pop_s[-1]
​
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (len(self.pop_s) or len(self.push_s))
​
​
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
