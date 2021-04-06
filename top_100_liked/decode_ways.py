class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        valid = set()
        for i in range(1, 27):
            valid.add(str(i))
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, int(s[0] in valid)
        for i in range(2, n+1):
            if(s[i-1:i] in valid):
                dp[i] += dp[i-1] 
            if(s[i-2:i] in valid):
                dp[i] += dp[i-2]
                
        return dp[n]
        
