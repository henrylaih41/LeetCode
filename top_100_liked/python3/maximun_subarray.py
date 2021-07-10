class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx, acc = -100000, 0
        for n in nums:
            acc = max(acc+n, n)
            maxx = max(maxx, acc)
        return maxx
