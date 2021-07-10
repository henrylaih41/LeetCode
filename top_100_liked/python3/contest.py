class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        target = [i for i in range(n)]
        count = 0
        while(count == 0 or not (perm == target)):
            print(perm, target)
            perm = self.op(perm)
        return count
    def op(self, perm):
        arr = [-1] * len(perm)
        n = len(perm)
        for i in range(len(perm)):
            if i % 2 == 0:
                arr[i] = perm[i // 2]
            if i % 2 == 1:
                arr[i] = perm[n // 2 + (i - 1) // 2]
        return arr

s = Solution()
s.reinitializePermutation(2)