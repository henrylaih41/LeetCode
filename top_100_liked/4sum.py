class Solution:
    ### O(n^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            for i_, j, k in self.threeSum(nums, i+1, len(nums)-1, target - nums[i]):
                result.append((nums[i], i_, j, k))
        return list(set(result))
    ### O(n) (if nums[i] is unique)
    
    def twoSum(self, nums, start, end, target):
        result, d = [], set()
        for i in range(start, end+1):
            if(target-nums[i] in d):
                result.append((target-nums[i], nums[i]))
            d.add(nums[i])
        return result
    
    ### O(n^2)
    def threeSum(self, nums, start, end, target):
        result = []
        for i in range(start, end+1):       
            for j, k in self.twoSum(nums, i+1, end, target-nums[i]):
                result.append((nums[i], j, k))
        return result
    
