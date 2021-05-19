class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if(len(s) == k+1):
                s.remove(nums[i-k-1])
            if(nums[i] in s):
                return True
            s.add(nums[i])
        return False
