class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        l = self.getlen(x)
        s = []
        while(len(s) < l//2):
            s.append(x % 10)
            x = x // 10
        if(l % 2):
            x = x // 10
        while(len(s)):
            if(s.pop() != x % 10):
                return False
            x = x // 10
        return True
    
    def getlen(self, x):
        poww, count = 10, 1
        while(x >= poww):
            poww *= 10
            count += 1
        return count
    
   
        
