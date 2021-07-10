class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while(l < r):
            while(l < r and nums[l] == nums[r-1]):
                r -= 1
            mid = (l+r)//2
            if(nums[mid] == target):
                return True
            ### left side
            if(nums[mid] >= nums[l]):
                if(nums[mid] > target and target >= nums[l]):
                    r = mid
                else:
                    l = mid + 1
            else:
                if(nums[mid] < target and target < nums[l]):
                    l = mid + 1
                else:
                    r = mid
        return False
