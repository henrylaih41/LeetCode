class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.getPrefix(nums)
        if(S > self.summ[0]):
            return 0
        self.pdp = [[-1] * (self.summ[0]+1) for _ in range(len(nums))]
        self.ndp = [[-1] * (self.summ[0]+1)for _ in range(len(nums))]
        return self.recur(nums, 0, S)
    
    ### dp is too slow
    def recur(self, nums, i, S):
        if(abs(S) > self.summ[i]):
            return 0
        dp = self.pdp if S >= 0 else self.ndp
        if(dp[i][S] != -1):
            return dp[i][S]
        ### base case
        if(i == len(nums)-1):
            ### edge case
            if(S == 0 and nums[i] == 0):
                return 2
            return 1 if abs(S) == nums[i] else 0
        pos = self.recur(nums, i+1, S-nums[i])
        neg = self.recur(nums, i+1, S+nums[i])
        dp[i][abs(S)] = pos + neg
        return dp[i][abs(S)]
        
    def getPrefix(self, nums):
        self.summ = [0]*len(nums)
        p = [abs(i) for i in nums]
        count = 0
        for i in range(len(nums)-1, -1, -1):
            count += p[i]
            self.summ[i] = count
