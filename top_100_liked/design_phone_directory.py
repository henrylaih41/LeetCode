from collections import deque
class PhoneDirectory:
​
    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.q = deque([i for i in range(maxNumbers)])
        self.s = set()
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if(len(self.q) == 0):
            return -1
        n = self.q.popleft()
        self.s.add(n)
        return n
​
    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return not (number in self.s)
​
    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if(number in self.s):
            self.q.appendleft(number) 
            self.s.discard(number)
        
​
​
# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
