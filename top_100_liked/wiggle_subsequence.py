class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ops = [operator.gt, operator.lt]
        maxx = 0
        for offset in range(2):
            count, last = 1, nums[0]
            for n in nums:
                if(last == n):
                    continue
                if(ops[(count+offset) % 2](last, n)):
                    count += 1
                    last = n
                else:
                    last = n
            maxx = max(maxx, count)
        return maxx
