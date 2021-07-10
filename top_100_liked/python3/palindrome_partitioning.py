class Solution:
    ### backtrack
    def partition(self, s):
        ### O(N^2)
        self.construct(s) 
        self.result, self.track = [], []
        ### O(N*2^N)
        self.backtrack(s, 0)
        return self.result
    
    def backtrack(self, s, head):
        if(head == len(s)):
            self.result.append(self.track.copy())
        for tail in range(head+1, len(s)+1):
            if(self.dp[head][tail]):
                self.track.append(s[head:tail])
                self.backtrack(s, tail)
                self.track.pop()
        
    ### Too slow
    def recur_partition(self, s: str) -> List[List[str]]:
        ### sss + s, sss + ss, ..., s + sss
        self.construct(s)
        self.d = {}
        result = self.recur(s, 0, len(s))
        final = set()
        for r in result:
            final.add(tuple(r))
        return final
    def recur(self, s, i, j):
        if((i, j) in self.d):
            return self.d[(i,j)]
        if(i+1 == j):
            return [[s[i:j]]]
        result = []
        for k in range(i+1, j):
            lis1 = self.recur(s, i, k)
            lis2 = self.recur(s, k, j)
            for l1 in lis1:
                for l2 in lis2:
                    result.append(l1 + l2)
        if(self.dp[i][j]):
            result.append([s[i:j]])
