class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if(k == 0):
            return
        n = len(nums)
        g = gcd(n, k)
        m = n // g
        kk = n // m
        for i in range(kk):
            j = i
            while(True):
                nxt = (j + k) % n
                self.swap(nums, i, nxt)
                j = nxt
                if(j == i):
                    break
        return
        
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
