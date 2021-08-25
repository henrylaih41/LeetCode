class Solution:
    ### fix one number x, we want to find all pairs that have a sum <= target - x
    ### we need a twoSum less than k subroutine
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if(len(nums) < 3):
            return 0
        result = 0
        nums.sort()
        for i in range(len(nums)):
            result += self.twoSumLessThanK(nums, i+1, len(nums)-1, target-nums[i])
        return result
    ### return the number of pairs in range [start, end] of nums that
    ### sum less than target
    ### @pre: nums should be sorted'
    ###              |->           <-|
    ### two pointer [1,2,3,4,5,6,7,8,9]
    def twoSumLessThanK(self, nums, start, end, target):
        count = 0
        l, r = start, end
        while(l < r):
            while(l < r and nums[l] + nums[r] >= target):
                r -= 1
            count += (r - l)
            l += 1
        return count
