# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
​
class Solution:
    def __init__(self):
        self.remain = []
        
    def read(self, buf: List[str], n: int) -> int:
        count = 0
        for i in range(min(n, len(self.remain))):
            buf[count] = self.remain[i]
            count += 1
        self.remain = self.remain[count:]
        buf4 = [""]*4
        while(count < n):
            r = read4(buf4)
            if(r == 0):
                return count
            for i in range(r):
                buf[count] = buf4[i]
                count += 1
                
        if(count > n):
            for i in range(count-n):
                self.remain.append(buf[n+i])
                buf[n+i] = ""
                count -= 1
        return count
            
            
        
