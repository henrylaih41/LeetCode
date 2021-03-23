class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.partition(nums, 0, n-1, n-k) 
        
    def partition(self, nums, low, high, target):
        pos = low
        ### nums[high] is the pivot
        for i in range(low, high):
            if(nums[i] <= nums[high]):
                self.swap(nums, pos, i)
                pos += 1
        self.swap(nums, pos, high)
        if(pos == target):
            return nums[pos]
        elif(pos > target):
            return self.partition(nums, 0, pos-1, target)
        else:
            return self.partition(nums, pos+1, high, target)
                
    
    def swap(self, nums, i, j):
        if(i == j):
            return
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
