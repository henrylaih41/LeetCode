class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 1, len(nums)

        # edge case
        if(n == 0):
            return 1

        while(i <= n):
            print(i)
            if(nums[i-1] >= 1 and nums[i-1] <= n and nums[nums[i-1]-1] != nums[i-1]):
                self.swap(nums, nums[i-1]-1, i-1)
                continue
            i += 1

        for i in range(len(nums)):
            if(nums[i] != i+1):
                return i+1
        ### edge case (easy to forget)
        return n + 1

    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
