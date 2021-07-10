class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = self.opt_linear(nums[2:-1]) + nums[0]
        r2 = self.opt_linear(nums[1:])
        return max(r1, r2)
        
    def linear(self, nums):
        if(len(nums) == 0):
            return 0
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])
    
    ### O(1) space
    def opt_linear(self, nums):
        if(len(nums) == 0):
            return 0
        no_steal, steal = 0, nums[0]
        for i in range(1, len(nums)):
            no_steal_tmp = max(no_steal, steal)
            steal = no_steal + nums[i]
            no_steal = no_steal_tmp
        return max(no_steal, steal)
