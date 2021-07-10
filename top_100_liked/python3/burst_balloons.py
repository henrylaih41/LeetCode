class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ex_nums = [1] + nums + [1]         
        dp = [[0]*(n+2) for _ in range(n+2)] 
        for i in range(1, n+1):
            dp[i][i] = ex_nums[i-1] * ex_nums[i] * ex_nums[i+1]
        """
        for j in range(1, n+1): # [1:n]
            for i in range(j-1, 0, -1): # [1:j-1]
                maxx = -math.inf
                for k in range(i, j+1): # [i:j] [1:n]
                    maxx = max(maxx, ex_nums[i-1]*ex_nums[k]*ex_nums[j+1]+dp[i][k-1]+dp[k+1][j])
                dp[i][j] = maxx
        """
        for i in range(n, 0, -1):
            for j in range(i+1, n+1, 1):
                maxx = -math.inf
                for k in range(i, j+1):
                     maxx = max(maxx, ex_nums[i-1]*ex_nums[k]*ex_nums[j+1]+dp[i][k-1]+dp[k+1][j])
                dp[i][j] = maxx
        return dp[1][n]
