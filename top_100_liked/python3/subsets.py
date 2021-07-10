class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 0):
            return [[]]
        result = self.subsets(nums[1:])
        n = len(result)
        for i in range(n):
            l = result[i].copy()
            l.append(nums[0])
            result.append(l)
        
        return result
