class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DP = [[0] * n for _ in range(m)]
        ## init
        DP[0][0] = grid[0][0]
        for i in range(1,n):
            DP[0][i] = DP[0][i-1] + grid[0][i]
        for i in range(1,m):
            DP[i][0] = DP[i-1][0] + grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]

        return DP[m-1][n-1]
