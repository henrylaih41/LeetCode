class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n for _ in range(2)]
        dp[(m-1)%2][n-1] = max(1, 1-dungeon[m-1][n-1])
        for i in range(n-2, -1, -1):
            dp[(m-1)%2][i] = max(1, dp[(m-1)%2][i+1] - dungeon[m-1][i])
        for i in range(m-2, -1, -1):
            print(dp)
            for j in range(n-1, -1, -1):
                if(j == n-1):
                    dp[i%2][j] = max(1, dp[(i+1)%2][j] - dungeon[i][j])
                else:
                    dp[i%2][j] = max(1, min(dp[(i+1)%2][j], dp[i%2][j+1]) - dungeon[i][j])
        return dp[0][0]
