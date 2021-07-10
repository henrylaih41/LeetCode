class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = math.inf, math.inf
        t1_profit, t2_profit = -math.inf, -math.inf
        ### this order means we have to complete exactly two transactions
        ### also we cannot buy and sell in the same day
        for p in prices:
            t2_profit = max(t2_profit, p - t2_cost)
            t2_cost = min(t2_cost, p - t1_profit)
            t1_profit = max(t1_profit, p - t1_cost)
            t1_cost = min(p, t1_cost)
        return max(0, t1_profit, t2_profit)
