class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if(n <= 2):
            return nums[-1]
        s, f = 0, 0
        while(1):
            while(f < n and (f <= s or nums[f] == nums[s])):
                f += 1
            if(f == n):
                break
            self.swap(s+1, f, nums)
            s += 2
                
        return nums[-1]
    
    
    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
