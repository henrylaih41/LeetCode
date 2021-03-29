class Solution:
    def clean(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 
    ### Top Down recursive approach
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = [[-1] * len(p) for _ in range(len(s))]
        self.s, self.p = s, self.clean(p)
        return self.recur(0, 0)
    
    def recur(self, i, j):
        dp, s, p = self.dp, self.s, self.p
        if(i == len(s) and j == len(p)):
            return 1
        if(p[j:] == "*"):
            return 1
        if(i >= len(s) or j >= len(p)):
            return 0
        if(dp[i][j] != -1):
            return dp[i][j] 
        if(p[j] == "*"):
            dp[i][j] = self.recur(i, j+1) or self.recur(i+1, j) or self.recur(i+1, j+1)
        elif(p[j] == "?" or s[i] == p[j]):
            dp[i][j] = self.recur(i+1, j+1)
        else:
            dp[i][j] = 0
        
        return dp[i][j]
