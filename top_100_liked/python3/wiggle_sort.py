import random 
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n == 1):
            return
        self.findKthElement(nums, 0, n, (n+1)//2)
        mapp = []
        for i in range(0, n, 2):
            mapp.append(i)
        for i in range(1, n, 2):
            mapp.append(i)
        mid = nums[(n+1)//2] if n % 2 else nums[(n+1)//2 - 1]
        print(mid, mapp, nums)
        i, l, r = 0, 0, n-1
        while(i <= r):
            if(nums[mapp[i]] < mid):
                self.swap(nums, mapp[i], mapp[l])
                l += 1
                i += 1
            elif(nums[mapp[i]] > mid):
                self.swap(nums, mapp[i], mapp[r])
                r -= 1
            else:
                i += 1
        
