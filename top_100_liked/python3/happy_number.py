class Solution:
    def isHappy(self, n: int) -> bool:
        sq = [i*i for i in range(10)]
        d = set()  
        
        while(n != 1):
            count = [0 for i in range(10)]
            nn = n
            while(nn != 0):
                count[nn % 10] += 1
                nn = nn // 10
            for i in range(10):
                nn += count[i]*sq[i]
            count = tuple(count)
            if(tuple(count) in d):
                return False
            d.add(count)
            n = nn
            
        return True
       
            
