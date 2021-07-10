class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, l, r = 0, 0, n-1
        while(i <= r):
            if(i > l and nums[i] == 0):
                self.swap(nums, i, l)
                l += 1
                continue
            if(i < r and nums[i] == 2):
                self.swap(nums, i, r)
                r -= 1
                continue
            i += 1

    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
