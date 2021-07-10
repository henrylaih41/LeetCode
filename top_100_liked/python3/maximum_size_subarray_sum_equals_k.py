class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        h = {}
        h[0] = 0
        summ, maxx = 0, -math.inf
        for i in range(1, len(nums)+1):
            summ += nums[i-1]
            if(h.get(summ-k, None) != None):
                maxx = max(maxx, i - h[summ-k])
            if(h.get(summ, None) == None):
                h[summ] = i
        return max(maxx, 0)
                
