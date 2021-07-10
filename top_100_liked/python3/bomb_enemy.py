class Solution:
    ### O(mn)
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        grid_count = [[0]*n for _ in range(m)]
        maxx = -math.inf
        for i in range(m):
            hit, update = 0, []
            for j in range(n+1):
                if(j == n or grid[i][j] == "W"):
                    for x, y in update:
                        grid_count[x][y] += hit
                    update = []
                    hit = 0
                elif(grid[i][j] == "E"):
                    hit += 1
                else:
                    update.append((i, j))
                    
        for j in range(n):
            for i in range(m+1):
                if(i == m or grid[i][j] == "W"):
                    for x, y in update:
                        maxx = max(maxx, grid_count[x][y]+hit)
                    update = []
                    hit = 0
                elif(grid[i][j] == "E"):
                    hit += 1
                else:
                    update.append((i, j))
        return max(0, maxx)
