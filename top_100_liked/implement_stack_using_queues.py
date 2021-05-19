from collections import deque
class MyStack:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = [deque(), deque()]
        self.filled = 0
​
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        filled = self.filled
        self.q[1-filled].appendleft(x)
        while(len(self.q[filled])):
            self.q[1-filled].appendleft(self.q[filled].pop())
        self.filled = 1 - self.filled
​
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q[self.filled].pop()
        
​
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[self.filled][-1]
​
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.q[self.filled])
        
​
​
# Your MyStack object will be instantiated and called as such:
