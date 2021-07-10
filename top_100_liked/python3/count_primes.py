import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if(n <= 1):
            return 0
        primes = [1 for _ in range(n)]
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
            if(not primes[i]):
                continue
            j = i * i
            while(j < n):
                primes[j] = 0
                j += i
        return sum(primes)
