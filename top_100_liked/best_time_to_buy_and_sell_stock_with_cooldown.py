class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n <= 1):
            return 0
        buy  = [0] * n
        sell = [0] * n
        
        buy[0], sell[0] = -prices[0], -math.inf
        buy[1], sell[1] = -min(prices[0], prices[1]), max(0, prices[1] - prices[0])
        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i], 0 - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[n-1]
