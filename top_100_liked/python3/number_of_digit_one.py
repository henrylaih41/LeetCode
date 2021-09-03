class Solution:
    def countDigitOne(self, n: int) -> int:
        k, p = 0, 1
        while(p <= n):
            p *= 10
            k += 1
        result, p = 0, 1
        ### [1, k]
        for i in range(1, k+1): 
            p *= 10
            t = n // p
            result += (t * p // 10)
            result += min(p // 10, max(0, (n % p) - (p // 10) + 1))
        return result
