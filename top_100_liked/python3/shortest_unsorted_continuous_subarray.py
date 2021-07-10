class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(math.inf) # nums[n] is inf
        nums.append(-math.inf) # nums[-1] is -inf
        s = [-1] # push -inf in bottom
        ### find left increasing
        for i in range(n):
            while(nums[i] < nums[s[-1]]):
                s.pop()
            s.append(i)
        i = 1
        while(i < len(s) and s[i] - s[i-1] == 1):
            i += 1
        l = s[i-1]
        s = [n] # push inf in bottom
        ### find right increasing
        for i in range(n-1, -1, -1):
            while(nums[i] > nums[s[-1]]):
                s.pop()
            s.append(i)
        i = 1
        while(i < len(s) and s[i-1] - s[i] == 1):
            i += 1
        r = s[i-1]
        #print(r, l)
        if(r <= l):
            return 0
        else:
            return r - l - 1
        
