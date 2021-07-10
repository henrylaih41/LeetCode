from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = []
        visited, distance = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        self.reached = [[0]*n for _ in range(m)]
        vcount  = 1
        self.dirr = [(0,1), (1,0), (-1,0), (0,-1)]
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    buildings.append((i, j))
                    
        for i, j in buildings:
            self.bfs(i, j, grid, distance, visited, vcount, m, n)
            vcount += 1
        
        minn = math.inf
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0 and self.reached[i][j] == len(buildings)):
                    minn = min(minn, distance[i][j])
        return minn if minn != math.inf else -1
    
    def bfs(self, i, j, grid, distance, visited, vcount, m, n):
        q = deque([(i, j, 0)])
        visited[i][j] = vcount
        while(len(q)):
            i, j, d = q.popleft()
            self.reached[i][j] += 1
            distance[i][j] += d
            for di, dj in self.dirr:
                if(i+di >= m or i+di < 0 or j+dj >= n or j+dj < 0):
                    continue
                if(visited[i+di][j+dj] != vcount and grid[i+di][j+dj] == 0):
                    visited[i+di][j+dj] = vcount
                    q.append((i+di, j+dj, d+1))
        
