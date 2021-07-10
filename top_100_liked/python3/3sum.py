class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found, ans = {}, []
        nums.sort()
        ### twoSums as subroutine
        for i, n in enumerate(nums):
            if(n in found):
                continue
            result = self.twoSum(nums[i+1:], 0 - n)
            found[n] = 1
            for l in result:
                ans.append((n,*l))
        return ans

    def twoSum(self, nums, target):
        mapp, found, result = {}, {}, []
        for n in nums:
            if(n in mapp and n not in found):
                result.append([n, target-n])
                found[n] = 1
            mapp[target-n] = 1 # dummy number
        return result
