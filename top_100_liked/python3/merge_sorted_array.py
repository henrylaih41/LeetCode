class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.shift(nums1, m, n)
        pt1, pt2, c = n, 0, 0
        while(pt1 < m+n and pt2 < n):
            if(nums1[pt1] <= nums2[pt2]):
                nums1[c] = nums1[pt1]
                pt1 += 1
            else:
                nums1[c] = nums2[pt2]
                pt2 += 1
            c += 1
            
        while(pt1 < m+n):
            nums1[c] = nums1[pt1]
            pt1 +=1
            c += 1
            
        while(pt2 < n):
            nums1[c] = nums2[pt2]
            pt2 += 1
            c += 1
        
        
    def shift(self, nums, m, n):
        for i in range(m-1, -1, -1):
            nums[n+i] = nums[i]
