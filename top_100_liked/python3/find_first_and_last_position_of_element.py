class Solution:
    ### l would be the smallest index satisfying cmp
    def sbinary_search(self, nums, target, cmp):
        l, r = 0, len(nums) # might not be found so r = n
        while(l < r):
            mid = (l+r)//2
            if(cmp(nums[mid], target)):
                r = mid
            else:
                l = mid + 1
        return l if (l < len(nums)) else -1

    ### r would be the biggest index satisfying cmp
    def bbinary_search(self, nums, target, cmp):
        l, r = -1, len(nums)-1
        while(l < r):
            mid = (l+r+1)//2 # so it prefer the right index
            if(cmp(nums[mid], target)):
                l = mid
            else:
                r = mid - 1
        return r # if not found r is default -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def cmp_start(a, b):
            return (a >= b)
        def cmp_end(a, b):
            return (a <= b)
        start = self.sbinary_search(nums, target, cmp_start)
        end   = self.bbinary_search(nums, target, cmp_end)
        ### start, end != -1 means element is found but still need to check if == target since cmp is >= or <=
        if(start != -1 and nums[start] != target):
            start = -1
        if(end != -1 and nums[end] != target):
            end = -1
        return [start, end]

    def OsearchRange(self, nums: List[int], target: int) -> List[int]:
        def cmp_start(a, b):
            return (a >= b)
        def cmp_end(a, b):
            return (a > b)
        start = self.sbinary_search(nums, target, cmp_start)
        end   = self.sbinary_search(nums, target, cmp_end)
        if(start != -1 and nums[start] != target):
            start = -1
        if(start == -1):
            return [-1, -1]
        if(start != -1 and end == -1):
            end = len(nums)

        return [start, end - 1]
