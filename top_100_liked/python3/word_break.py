class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ### dp[i] stores whether s[:i] can be work break
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                if(s[j:i] in wordDict and dp[j]):
                    dp[i] = 1
        return dp[n]
