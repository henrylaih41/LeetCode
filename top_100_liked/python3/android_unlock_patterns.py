class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        d = {}
        arr = [(1,3), (1,7), (1,9), (2,8), (3,7), (3,9), (4,6), (7,9)]
        for i, j in arr:
            k = (i+j) // 2
            d[(i, j)] = k
            d[(j, i)] = k
        self.d = d
        self.result = 0
        self.backtrack(set(), 0, n, m)
        return self.result
    
    def backtrack(self, seq, last, n, m):
        if(len(seq) >= m and len(seq) <= n):
            self.result += 1
        if(len(seq) == n):
            return
        
        for i in range(1, 10):
            if(i not in seq and ((last, i) not in self.d or self.d[(last, i)] in seq)):
                seq.add(i)
                self.backtrack(seq, i, n, m)
                seq.remove(i)
    
