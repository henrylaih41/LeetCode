class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for n in coins:
                if(n > i):
                    break
                dp[i] = min(dp[i], dp[i-n] + 1)
        
        return -1 if dp[amount] == math.inf else dp[amount]
