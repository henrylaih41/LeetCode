class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, n in enumerate(nums):
            if(n not in mapp):
                mapp[target - n] = i
            else:
                return [i, mapp[n]]
