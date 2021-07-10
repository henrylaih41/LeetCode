class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        visited = [[0]*n for _ in range(m)]
        dirr = [[0,1], [1,0], [0,-1], [-1,0]]
        self.l, self.r, self.t, self.d = x, x, y, y
        self.dfs(x, y, image, dirr, m, n, visited)
        return (self.r - self.l + 1) * (self.d - self.t + 1)
    
    def dfs(self, i, j, image, dirr, m, n, visited):
        visited[i][j] = 1
        for di, dj in dirr:
            if(i+di == m or i+di < 0 or j+dj < 0 or j+dj == n):
                continue
            if(not visited[i+di][j+dj] and int(image[i+di][j+dj])):
                self.dfs(i+di, j+dj, image, dirr, m, n, visited)
        
        self.l = min(self.l, i)
        self.r = max(self.r, i)
        self.t = min(self.t, j)
        self.d = max(self.d, j)
