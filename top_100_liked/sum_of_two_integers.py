class Solution:
    def getSum(self, a: int, b: int) -> int:
        if(a == 0 or b == 0):
            return a if a else b
        ### x >= y
        if(abs(b) > abs(a)):
            a, b = b, a
        x, y = abs(a), abs(b)
        result = None
        ### ++ or --
        if((a * b) > 0):
            result = x ^ y
            carry  = (x & y) << 1
            while(carry):
                tmp = result
                result ^= carry
                carry = (tmp & carry) << 1
        ### -+ or +-
        else:
            result = x ^ y
            borrow = (~x & y) << 1
            while(borrow):
                tmp = result
                result ^= borrow
                borrow = (~tmp & borrow) << 1
        if(a > 0):
            return result
        return -result
