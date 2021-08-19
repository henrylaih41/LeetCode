class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.result = 0
        self.mapp = {"0" : "0",
                     "1" : "1",
                     "6" : "9",
                     "8" : "8",
                     "9" : "6"}
        if(len(low) == len(high)):
            self.findStrobogrammatic(len(low), low, high)
        else:
            self.findStrobogrammatic(len(low), low, "".join(["9"] * len(low)))
            for i in range(len(low)+1, len(high)):
                self.findStrobogrammatic(i, "".zfill(i), "".join(["9"] * i))
            self.findStrobogrammatic(len(high), "".zfill(len(high)), high)
            
        return self.result
    def findStrobogrammatic(self, n: int, low, high) -> List[str]:
        self.low = low
        self.high = high
        self.backtrack("", (n+1)//2, n % 2)
        #if(n == 1):
        #    return ["0", "1", "8"]    
    
    def backtrack(self, s, n, odd):
        if(len(s) == n):
            self.complete(s, odd)
            return
        if(len(s) == n-1 and odd):
            for i in ["0", "1", "8"]:
                self.backtrack(s + i, n, odd)
        else:   
            for i in ["0", "1", "6", "8", "9"]:
                ### no leading zero
                if(i == "0" and len(s) == 0):
                    continue
                self.backtrack(s + i, n, odd)
        
    def complete(self, s, odd):
        ss = ""
        inv = s
        if(odd):
            inv = inv[:-1]
        for c in inv[::-1]:
            ss += self.mapp[c]
        if((s+ss) >= self.low and (s+ss) <= self.high):
            self.result += 1
