class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirr = [(0,1), (0,-1), (1,0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)] 
        count = 0
        for x in range(n):
            for y in range(m):
                if(not visited[y][x] and grid[y][x] == "1"):
                    self.dfs(x, y, dirr, visited, m, n, grid)
                    count += 1
                
        return count
    def isValid(self, x, y, m, n, grid):
        return (x >= 0 and x < n and y >= 0 and y < m and grid[y][x] == "1")
    
    def dfs(self, x, y, dirr, visited, m, n, grid):
        visited[y][x] = 1
        for dx, dy in dirr:
            if(self.isValid(x+dx, y+dy, m, n, grid) and not visited[y+dy][x+dx]):
                self.dfs(x+dx, y+dy, dirr, visited, m, n, grid)
                
                
