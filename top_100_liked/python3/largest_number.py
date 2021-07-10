import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = [str(i) for i in nums]
        snums.sort(key=functools.cmp_to_key(self.cmp), reverse=True)
        print(snums)
        if(snums[0][0] == "0"):
            return "0"
        return "".join(snums)
    
    ### two string
    def cmp(self, a, b):
        x, y = a, b
        xt, yt, count = 0, 0, 0
        while(count < len(a) + len(b)):
            if(xt >= len(x)):
                x, xt = b, 0
            if(yt >= len(y)):
                y, yt = a, 0
            if(x[xt] > y[yt]):
                return 1
            elif(y[yt] > x[xt]):
                return -1
            xt += 1
            yt += 1
            count += 1
        return 0
            
            
