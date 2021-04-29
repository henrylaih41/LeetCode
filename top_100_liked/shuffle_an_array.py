import random
class Solution:
​
    def __init__(self, nums: List[int]):
        self.arr = list(nums)
​
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.arr)
        
​
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        s = list(self.arr)
        for i in range(len(s)-1):
            r = random.randint(i, len(s)-1)
            s[r], s[i] = s[i], s[r]
        return s
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
