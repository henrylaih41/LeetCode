class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m, self.n = len(matrix), len(matrix[0])
        self.dp = [[-1]*self.n for _ in range(self.m)]
        self.dirr = [(0,1), (0,-1), (1,0), (-1,0)]
        self.maxx = -math.inf
        
        for i in range(self.m):
            for j in range(self.n):
                if(self.dp[i][j] == -1):
                    self.maxx = max(self.dfs(matrix, i, j), self.maxx)
        
        return self.maxx
    
    def dfs(self, matrix, i, j):
        if(self.dp[i][j] != -1):
            return self.dp[i][j]
        
        for di, dj in self.dirr:
            if(i + di >= self.m or i + di < 0 or j + dj >= self.n or j + dj < 0):
                continue
            if(matrix[i+di][j+dj] > matrix[i][j]):
                self.dp[i][j] = max(self.dfs(matrix, i+di, j+dj)+1, self.dp[i][j])
    
        self.dp[i][j] = max(self.dp[i][j], 1)
        return self.dp[i][j]
