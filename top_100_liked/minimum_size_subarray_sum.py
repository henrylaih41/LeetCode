class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        head, summ, minn = 0, 0, math.inf
        for i, tail in enumerate(nums):
            if(summ < target):
                summ += tail
            while(summ >= target):
                minn = min(minn, i - head + 1)
                summ -= nums[head]
                head += 1
        return minn if minn != math.inf else 0
