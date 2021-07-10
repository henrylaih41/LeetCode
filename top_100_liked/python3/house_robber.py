class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = nums[0]
        
        for i in range(1, n):
            ### don't have to check max(0, ...) because nums[i] is guarantee to be >= 0
            dp[i][0] = dp[i-1][1] + nums[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            
        return max(dp[n-1][0], dp[n-1][1])
