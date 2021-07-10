from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 1):
            return [nums[0]]
        d = deque() 
        ans = []
        for i in range(k):
            while(len(d) != 0 and nums[i] > d[-1][1]):
                d.pop()
            d.append((i, nums[i]))
        ans.append(d[0][1])
        
        for i, n in enumerate(nums[k:]):
            j = i + k
            while(len(d) != 0 and n >= d[-1][1]):
                d.pop()
            d.append((j, n))
            
            while(d[0][0] <= j - k):
                d.popleft()
            
            ans.append(d[0][1])
        
        return ans
