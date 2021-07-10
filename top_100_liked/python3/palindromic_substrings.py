class Solution:
    def countSubstrings(self, s: str) -> int:
        n, count = len(s), 0
        ### i 0~n-1, j 1~n
        dp = [[0]*(n+1) for _ in range(n)]
        ### init
        for i in range(n):
            dp[i][i+1] = 1
        for i in range(n-1):
            if(s[i] == s[i+1]):
                dp[i][i+2] = 1
        #print(dp)
        ### constuct dp table
        for j in range(3, n+1):
            for i in range(0, n-j+1):
                k = j+i
                dp[i][k] = (s[k-1] == s[i]) and dp[i+1][k-1]
        for i in range(n):
            for j in range(1, n+1):
                count += dp[i][j] 
        #print(dp)
        return count
