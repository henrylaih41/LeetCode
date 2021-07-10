class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx, s = 0, set(nums)
        for n in s:
            if(n-1 in s):
                continue
            else:
                count = 0
                while(n in s):
                    count += 1
                    n += 1
                maxx = max(maxx, count)
        return maxx
