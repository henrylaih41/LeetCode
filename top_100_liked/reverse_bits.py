class Solution:
    def reverseBits(self, n: int) -> int:
        summ, k, a = 0, 1 << 31, 1 << 31
        while(1):
            summ += ((n//k) % 2) * (a // k)
            k >>= 1
            if(k == 0):
                break
        return summ
