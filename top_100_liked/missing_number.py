class Solution:
    def v1missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(None) # a space for index n 
        ### visite the node in nums[i]
        for i in range(n):
            i = nums[i]
            while(i != None and i != -1):
                nxt = nums[i]
                nums[i] = -1
                i = nxt
        for i in range(n+1):
            if(nums[i] != -1):
                return i
    # XOR
    def v2missingNumber(self, nums):
        x = len(nums)
        for i in range(len(nums)):
            x ^= i
            x ^= nums[i]
        return x
        
    # Sum (Fastest)
    def missingNumber(self, nums):
        x = len(nums)*(len(nums)+1)//2
        for n in nums:
            x -= n
        return x
            
