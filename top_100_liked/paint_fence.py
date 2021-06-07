class Solution:
    def corrent_numWays(self, n: int, k: int) -> int:
        # dp[n] = (dp[n-1] + dp[n-2]) * (k-1)
        if(n == 1):
            return k
        dp = [0] * (n+1)
        dp[1] = k
        dp[2] = k*k
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        return dp[n]
    
    ### wrong definition version
    def numWays(self, n, k):
        self.count = 0
        self.backtrack([None], n, k, 1)
        self.dp = [0] * (n+1)
        self.dp[1] = k
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] * (k-1)
        print(self.count, self.recur(n, k))
        
    def recur(self, n, k):
        if(n == 1):
            return k
        if(n == 2):
            return k*k
        return (self.recur(n-1, k) + self.dp[n-2])*(k-1)
    
    def backtrack(self, comb, n, k, left):
        if(left < 0):
            return
        if(len(comb) == (n+1)):
            self.count += 1
            return
        for i in range(1, k+1):
            remain = left-1 if(i == comb[-1]) else left
            comb.append(i)
            self.backtrack(comb, n, k, remain)
            comb.pop()
        
