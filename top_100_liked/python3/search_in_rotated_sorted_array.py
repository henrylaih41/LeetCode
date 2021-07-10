class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if(n <= 1):
            return -1 if (n == 0 or target != nums[0]) else 0
        if(nums[0] < nums[-1]):
            k = 0
        else:
            ### search for k
            l, r = 0, n - 1 # since there is always a num satisfying the condition
            while(l < r):
                mid = (l+r)//2
                if(nums[mid] <= nums[-1]):
                    r = mid
                else:
                    l = mid + 1
            k = n - l
        ### normal binary search with mapping
        l, r = 0, n # might not find val satisfying val >= target (l would be n)
        while(l < r):
            mid = (l+r)//2
            val = nums[(mid - k + n) % n]
            if(val >= target):
                r = mid
            else:
                l = mid + 1
        if(l < n and nums[(l - k + n) % n] == target):
            return (l - k + n) % n
        return -1
