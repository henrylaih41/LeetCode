from heapq import heappush, heappop
class Solution:
    ### lets say prime = [2, 3, 5, 7]
    ### maintain a list for each prime
    ### 2, 2 * 2, 2 * 3, ..., 2 * n
    ### 3, 3 * 2, 3 * 3, ..., 3 * n
    ### 5, 5 * 2, 5 * 3, ..., 5 * n
    ### 7, 7 * 2, 7 * 3, ..., 7 * n
    ### maintain a min heap? always pop the smallest candiate out
    ### [2, 3, 5 ,7] => [3, 4, 5, 7] => [4, 5, 6, 7] => [5, 6, 7, 8] ...
    ### so the heap would always at most have n elements
    ### we use a set to maintain the number we already putted in the heap
    ### we need to check if p * i, whether i is a prime
    ### brute, we get all primes before n (O(n^2))
    ### or p1^x * p2^y * p3^z * ... * 
    ### TLE version
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = set()
        heap = [1] # (value, p)
        while(True):
            result = heappop(heap)
            for p in primes:
                if(result * p not in seen):
                    seen.add(result * p)
                    heappush(heap, result * p)
                ### need this line to pass (why?)
                if(result % p == 0):
                    break
            n -= 1
            if(n == 0):
                return result
    ### still TLE
    def v1nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        primes_index = [0] * k
        ans = [1]
        for i in range(n-1):
            minn = math.inf
            for i in range(k):
                cand = ans[primes_index[i]] * primes[i]
                minn = min(minn, cand)
            for i in range(k):
