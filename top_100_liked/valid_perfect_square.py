class Solution:
    def v1isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num+1
        
        while(l < r):
            mid = (l + r) // 2
            if(mid * mid == num):
                return True
            elif(mid * mid > num):
                r = mid
            else:
                l = mid + 1
        return False
    
    ### newton's method
    def isPerfectSquare(self, num):
        ### let the first seed be bigger than sqrt(num)
        x = num
        while(x * x > num):
            x = (x + num // x) // 2
        return x * x == num
