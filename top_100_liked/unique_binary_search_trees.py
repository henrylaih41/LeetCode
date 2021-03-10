class Solution:
    def numTrees(self, n: int) -> int:
        if(n <= 1):
            return 1
        DP = [-1] * (n+1)
        DP[0], DP[1] = 1, 1
        return self.recur(n, DP)
    def recur(self, n, DP):
        if(DP[n] != -1):
            return DP[n]
        summ = 0
        for i in range(1, n+1):
            summ += self.recur(i-1, DP) * self.recur(n-i, DP)
        DP[n] = summ
        return summ

    def validParenthess(self, n):
        if(n <= 1):
            return 1
        DP = [-1] * (n+1)
        DP[0], DP[1] = 1, 1
        return self.util(n, DP)

    def util(self, n, DP):
        ### (0)*util(n-1) + ... + (n-1) * 0
        if(DP[n] != -1):
            return DP[n]
        summ = 0
        for i in range(0, n):
            summ += self.util(i, DP) * self.util(n-i-1, DP)
        DP[n] = summ
        return summ

s = Solution()
for i in range(20):
    print(s.validParenthess(i))
