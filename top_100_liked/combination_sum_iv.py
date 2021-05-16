class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.dp = [0] * (target+1)
        ### self.dp[0] = 1 one way to be empty
        ### base case
        self.dp[0] = 1
        ### construct dp[table]
        for i in range(target+1):
            for j in range(len(nums)):
                if(i - nums[j] < 0):
                    break
                self.dp[i] += self.dp[i - nums[j]]
                
        return self.dp[target]
