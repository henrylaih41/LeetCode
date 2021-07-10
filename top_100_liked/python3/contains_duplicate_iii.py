from collections import deque
​
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d, div = {}, t+1
        for i in range(len(nums)):
            if(i > k):
                del d[nums[i-k-1]//div]
            idx = nums[i]//div
            if(d.get(idx, None) != None):
                return True
            else:
                d[idx] = nums[i]
                if(d.get(idx-1, None) != None and nums[i] - d.get(idx-1) <= t):
                    return True
                if(d.get(idx+1, None) != None and d.get(idx+1) - nums[i] <= t):
                    return True
        return False
            
            
