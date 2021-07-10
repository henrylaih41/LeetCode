class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        costs = [math.inf] * k
        profits = [-math.inf] * k
        for p in prices:
            for i in reversed(range(k)):
                profits[i] = max(profits[i], p - costs[i])
                if(i):
                    costs[i] = min(costs[i], p - profits[i-1])
                else:
                    costs[i] = min(costs[i], p)
        maxx = -math.inf
        for i in range(k):
            maxx = max(maxx, profits[i])
        return max(0, maxx)
