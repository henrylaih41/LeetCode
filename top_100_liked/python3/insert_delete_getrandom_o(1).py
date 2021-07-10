import random
class RandomizedSet:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d, self.arr = {}, []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val in self.d):
            return False
        self.arr.append(val)
        self.d[val] = len(self.arr)-1
        return True
    
    def remove(self, val: int) -> bool:
        if(val not in self.d):
            return False
        tmp = self.arr[-1]
        self.d[tmp] = self.d[val]
        self.arr[self.d[val]] = tmp
        del self.d[val]
        self.arr.pop()
        return True
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
​
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]
        """
        Get a random element from the set.
        """
        
​
​
# Your RandomizedSet object will be instantiated and called as such:
