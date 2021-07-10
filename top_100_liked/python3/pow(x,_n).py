class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign, result = 1, 1
        if(n < 0):
            sign = -1
            n = -n
        poww, nn = 1, x
        while(n != 0):
            while(poww * 2 <= n):
                poww *= 2
                nn *= nn
            result *= nn
            n -= poww
            nn = x
            poww = 1
        if(sign == 1):
            return result
        elif(sign == -1):
            return 1/result
