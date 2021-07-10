class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        for i in range(len(nums)):
            if(nums[i] == prev):
                nums[i] = None
            else:
                prev = nums[i]
        print(nums)
        head = 0
        for i in range(len(nums)):
            if(nums[i] != None):
                print(nums[i])
                nums[head] = nums[i]
                head += 1
        return head
