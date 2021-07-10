class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = 0
        for n in nums:
            summ += n
        if(summ % 2):
            return False
        self.dp = [[-1] * summ for _ in range(len(nums))]
        for i in range(len(nums)):
            self.dp[i][0] = 1
        return self.knapsack(nums, len(nums)-1, summ//2)
    
    def knapsack(self, nums, i, target):
        if(target < 0 or i < 0):
            return 0
        if(self.dp[i][target] != -1):
            return self.dp[i][target]
        self.dp[i][target] = self.knapsack(nums, i-1, target) or self.knapsack(nums, i-1, target-nums[i])
        return self.dp[i][target]
         
