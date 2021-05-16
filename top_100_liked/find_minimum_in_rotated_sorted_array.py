class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while(l < r):
            mid = (l+r)//2
            if(mid < len(nums)-1 and nums[mid] > nums[mid+1]):
                return nums[mid+1]
            if(nums[mid] >= nums[l]):
                l = mid+1
            else:
                r = mid
            
        return nums[0]
