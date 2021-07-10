class Solution:
    def wiggleSort(self, nums):
        if(len(nums) < 2):
            return 
        k = (len(nums)-1) // 2
        mid = self.findKthLargest(nums, k+1)
        nm = [0]*len(nums)
        count = 1
        for i in range(len(nums)):
            nm[i] = count 
            count += 2
            if(count >= len(nums)):
                count = 0
        ### 3 way partition
        i, j, k = 0, 0, len(nums)-1
        while(j <= k):
            if(nums[nm[j]] > mid):
                self.swap(nums, nm[i], nm[j])
                i += 1
                j += 1
            elif(nums[nm[j]] < mid):
                self.swap(nums, nm[j], nm[k])
                k -= 1
            else:
                j += 1
        
​
    def v1wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ### Quick select into two piles
        k = (len(nums)-1) // 2
        mid = self.findKthLargest(nums, k+1)
        i, j = 0, 0
        #print(nums, mid)
        for _ in range(k+1):
            if(nums[j] == mid):
                self.swap(nums, i, j)
                i += 2
            j += 2
            if(j > k):
                j = 1
            if(i > k):
                i = 1 
        j = len(nums) - 1 - len(nums)%2 ### first odd from tail
        i = j
        for _ in range(len(nums)-k-1):
            if(nums[j] == mid):
                self.swap(nums, i, j)
                i -= 2
            j -= 2
            if(j < k+1):
                j = len(nums) - 2 + len(nums)%2
            if(i < k+1):
                i = len(nums) - 2 + len(nums)%2
        #print(nums, k)
