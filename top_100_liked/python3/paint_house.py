class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0]*3 for _ in range(len(costs))]
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
        return min(dp[-1][0], dp[-1][1], dp[-1][2])
