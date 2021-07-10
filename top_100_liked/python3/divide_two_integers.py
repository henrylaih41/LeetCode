class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend == 0):
            return 0
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor > 0 else -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        count = self.binary_find(dividend, divisor)
        
        if(sign1 ^ sign2):
            count = -count
        if(count > (1 << 31) - 1 or count < -(1 << 31)):
            return (1 << 31) - 1
        return count
    
    def binary_find(self, dividend, divisor):
        count = 0
        while(dividend >= divisor):
            poww, v = 1, divisor 
            while(v + v <= dividend):
                poww += poww
                v    += v
            count += poww
            dividend -= v
        return count
