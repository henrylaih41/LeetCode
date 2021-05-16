class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while(l < r):
            ### this might cause us to miss the lowest value if we only check
            ### nums[mid] > nums[mid+1] (if r land on lowest and nums[l] == nums[r-1])
            while(l < r and nums[l] == nums[r-1]):
                r -= 1
            mid = (l+r)//2
            ### if mid land on the lowest value, and the left region is nums[l] == nums[r-1]
            ### then we would miss the edge so we check the other condition below
            if(mid < len(nums)-1 and nums[mid] > nums[mid+1]):
                return nums[mid+1]
            ### This is needed
            if(mid > 0 and nums[mid] < nums[mid-1]):
                return nums[mid]
            if(nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid
        ### we get here if nums is sorted
        return nums[0]
