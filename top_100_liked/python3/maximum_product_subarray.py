class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-math.inf, math.inf] for _ in range(n)]
        maxx, dp[0][0], dp[0][1] = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if(nums[i] >= 0):
                dp[i][0] = max(dp[i-1][0] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i][0] = max(dp[i-1][1] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][0] * nums[i], nums[i])
            maxx = max(maxx, dp[i][0])
            
        return maxx
            
