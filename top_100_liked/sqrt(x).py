class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binary_search(x)
        
    def linear_search(self, x):
        count = 0
        while(count*count <= x):
            count += 1
        return count-1
    
    def binary_search(self, x):
        l, r = 0, x+1 #
        while(l < r):
            mid = (l+r)//2
            if(mid*mid > x):
                r = mid
            else:
                l = mid+1
        return l-1
        
