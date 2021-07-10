class Solution:
    def v1numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * n for _ in range(m)]
        ### base 
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, min(m, n)):
            dp[i][i] = 1 if (s[i] == t[i] and dp[i-1][i-1]) else 0
            
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]
            if(s[i] == t[0]):
                dp[i][0] += 1
                
        for j in range(1, n):
            for i in range(j+1, m):
                dp[i][j] = dp[i-1][j]
                if(s[i] == t[j]):
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[m-1][n-1]
    
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        if(n > m):
            return 0
        ### only need to store previous row
        dp = [[0]*2 for _ in range(m)]
        ### base
        dp[0][0] = 1 if s[0] == t[0] else 0
        ### init first row
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]
            if(s[i] == t[0]):
                dp[i][0] += 1
        for j in range(1, n):
            for i in range(j, m):
                if(i == j):
                    dp[i][i%2] = 1 if (s[i] == t[i] and dp[i-1][(i-1)%2]) else 0
                    continue 
                dp[i][j%2] = dp[i-1][j%2]
                if(s[i] == t[j]):
                    dp[i][j%2] += dp[i-1][(j-1)%2]
        return dp[m-1][(n-1)%2]
        
        
        
        
