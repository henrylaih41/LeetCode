class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        # base case
        if(n == 1):
            return [[nums[0]]]
        comb = self.permute(nums[1:])
        m = len(comb[0])
        for c in comb:
            for i in range(m+1):
                nc = c.copy()
                nc.insert(i, nums[0])
                result.append(nc)
        return result
