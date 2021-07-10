class Solution:
    def __init__(self):
        self.memo = {}
        self.result = []
    def v1getFactors(self, n: int) -> List[List[int]]:
        if(n in self.memo):
            return self.memo[n]
        if(n == 1):
            return []
        result = []
        for f in range(2, int(sqrt(n))+1):
            if(n % f == 0):
                for fl in self.getFactors(n // f):
                    if(fl[0] >= f):
                        result.append([f] + fl)
                result.append([f, n // f])
        self.memo[n] = result
        return result
    
    def getFactors(self, n):
        if(n == 1):
            return []
        self.backtrack([], n)
        return self.result
    
    def backtrack(self, comb, n):
      
        
