class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count, prev = 0, 0, None
        for i in range(len(nums)):
            if(prev != nums[i]):
                count = 1
                nums[j] = nums[i]
                j += 1
            elif(prev == nums[i]):
                if(count < 2):
                    count += 1
                    nums[j] = nums[i]
                    j += 1
            prev = nums[i]
        return j
