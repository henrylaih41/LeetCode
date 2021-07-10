from collections import defaultdict
import random
class RandomizedCollection:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.mapping = defaultdict(lambda: set())
​
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = (len(self.mapping[val]) == 0)
        self.mapping[val].add(len(self.items))
        self.items.append(val)
        return flag
​
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if(len(self.mapping[val]) == 0):
            return False
        pos, last = self.mapping[val].pop(), self.items[-1]
        if(pos != len(self.items)-1):
            self.mapping[last].discard(len(self.items)-1)
            self.mapping[last].add(pos)
            self.items[pos] = last
        self.items.pop()
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.items[random.randint(0, len(self.items)-1)]
​
​
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
