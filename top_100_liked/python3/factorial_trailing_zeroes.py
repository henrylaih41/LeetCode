class Solution:
    def trailingZeroes(self, n: int) -> int:
        twos = self.logCount(n, 2)
        fives = self.logCount(n, 5)
        return min(twos, fives)
        
    def logCount(self, n, b):
        k, count = b, 0
        while(n >= k):
            count += (n // k)
            k *= b
        return count
