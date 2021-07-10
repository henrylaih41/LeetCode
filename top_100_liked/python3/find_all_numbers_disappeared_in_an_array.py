class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result, n, maxx = [], len(nums), len(nums) + 1
        for i in range(n):
            nums[i] *= maxx
        for i in range(n):
            idx = (nums[i]//maxx)-1
            nums[idx] += 1
        for i in range(n):
            if(nums[i] % maxx == 0):
                result.append(i+1)
        return result
            
