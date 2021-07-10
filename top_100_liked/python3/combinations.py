class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.backtrace([], 1, n, k)
        return self.result
    
    def backtrace(self, comb, start, n, k):
        if(k == 0):
            self.result.append(list(comb))
            return
        for i in range(start, n+1):
            self.backtrace(comb + [i], i+1, n, k-1)
