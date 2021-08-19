class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.result = []
        self.mapp = {"0" : "0",
                     "1" : "1",
                     "6" : "9",
                     "8" : "8",
                     "9" : "6"}
        self.backtrack("", (n+1)//2, n % 2)
        #if(n == 1):
        #    return ["0", "1", "8"]
        return self.result
    
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
        self.result.append(s + ss)
