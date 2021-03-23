class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 0, maxSum+1
        while(l < r):
            mid = (l+r)//2
            if(self.vfunc(mid, index, n) <= maxSum):
                l = mid + 1
            else:
                r = mid
        return l-1
        
        
    def vfunc(self, k, i, n):
        rsum = max(n-i-k, 0) 
        if(n-1 >= i + k - 1):
            rsum += (k+1)*k/2
        else:
            rsum += (2*k-n+1+i)*(n-i)/2
        lsum = max(i-k+1, 0) 
        if(i-k+1 >= 0):
            lsum += (k+1)*k/2
        else:
            lsum += (2*k - i)*(i+1)/2
        #print(k, i, n, rsum, lsum, rsum+lsum-k)
        return rsum + lsum - k
