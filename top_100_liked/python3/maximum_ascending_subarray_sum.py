class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if(nums[i] > nums[i-1]):
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        maxx = 0
        for i in range(n):
            maxx = max(maxx, dp[i])
            
        return maxx
