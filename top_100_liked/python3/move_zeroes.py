class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first zero, starting from 0 index
        # if not found return
        s = self.findZero(nums, 0)
        if(s == -1):
            return 
        for i in range(s+1, len(nums)):
            if(nums[i] != 0):
                nums[i], nums[s] = nums[s], nums[i]
                s += 1 # the next must still be zero
        return 
    def findZero(self, nums, s):
        while(s < len(nums) and nums[s] != 0):
            s += 1
        if(s < len(nums)):
            return s
        else:
            return -1
