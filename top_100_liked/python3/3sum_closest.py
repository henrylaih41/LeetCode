class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            v = target - nums[i]
            while(j < k):
                s = nums[j] + nums[k]
                if(abs(s + nums[i] - target) < abs(closest - target)):
                    closest = s + nums[i]
                if(s > v):
                    k -= 1
                elif(s < v):
                    j += 1
                else:
                    return target
        return closest
