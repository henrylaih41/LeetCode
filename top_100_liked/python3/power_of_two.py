class Solution:
    def v1isPowerOfTwo(self, n: int) -> bool:
        if(n <= 0):
            return False
        if(n < 1 and n > 0):
            n = 1 / n
        x = 2
        while(x * x <= n):
            x = x * x
        if(x == n):
            return True
        while(n != 1):
            if(n < x):
                x = int(sqrt(x))
                continue
            if(n % x):
                return False
            n = n // x
        return True
    
    def isPowerOfTwo(self, n):
        if(n <= 0):
            return False
        # n - (n & -n) == n & (n-1)
        return n == (n & -n)
