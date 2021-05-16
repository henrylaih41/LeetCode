class Solution:
    def v1rangeBitwiseAnd(self, left: int, right: int) -> int:
        if(left == right):
            return left
        c = (~left) & right
        n = 1
        while(n <= c):
            n <<= 1
        n >>= 1
        return (left // n) * n
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while(left < right):
            right = right & (right-1)
        return right
