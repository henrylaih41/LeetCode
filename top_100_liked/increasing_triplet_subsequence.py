class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums) < 3):
            return False
        head = [nums[0], math.inf]
        for n in nums:
            if(n < head[0]):
                head[0] = n
            elif(n > head[0] and n < head[1]):
                head[1] = n
            elif(n > head[1]):
                return True
        return False
