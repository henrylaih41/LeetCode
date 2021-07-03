class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if(obstacleGrid[i][0]):
                break
            dp[i][0] = 1
        for i in range(n):
            if(obstacleGrid[0][i]):
                break
            dp[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                ### dp[i][j] = 0
                if(obstacleGrid[i][j] == 1):
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
                
