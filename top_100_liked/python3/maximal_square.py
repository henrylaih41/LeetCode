class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxx = 0
        # scan for ones for edge cases (m == 1or n == 1)
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == "1"):
                    maxx = 1
        # base case
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if int(matrix[i][j]) == 0 else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                maxx = max(maxx, dp[i][j])
    
        return maxx**2
        
                    
        
