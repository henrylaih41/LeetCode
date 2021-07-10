class Solution:
    def find(self, LIS, num, length):
        l, r = 0, length
        while(l < r):
            mid = (l+r)//2
            if(LIS[mid] >= num):
                r = mid
            else:
                l = mid + 1
        return r
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ### possible len 1~n
        LIS = [0] * (n+1)
        LIS[0] = nums[0]
        length = 1
        for n in nums[1:]:
            r = self.find(LIS, n, length)
            LIS[r] = n
            if(r == length):
                length += 1
        
        return length
        
