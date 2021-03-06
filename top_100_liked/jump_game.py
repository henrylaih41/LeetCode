class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end, n = 0, len(nums)

        for i in range(n):
            if(i > end):
                return False
            if(i == n-1):
                return True
            end = max(end, i + nums[i])
