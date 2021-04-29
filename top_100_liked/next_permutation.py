class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### find the element to swap
        prev = -math.inf
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] < prev):
                prev = i
                break
            prev = nums[i]
            if(i == 0):
                nums.sort()
                return 
        ### swap with first element bigger than prev
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] > nums[prev]):
                self.swap(nums, i, prev)
                break
        ### reverse
        self.reverse(nums, prev+1, len(nums)-1)
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def reverse(self, nums, i, j):
        while(i < j):
            self.swap(nums, i, j)
            i += 1
            j -= 1
