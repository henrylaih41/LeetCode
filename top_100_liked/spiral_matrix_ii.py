class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        visited = [[0]*n for _ in range(n)]
        dirr = [(0,1), (1,0), (0,-1), (-1,0)]
        i, j, d = 0, 0, 0
        for k in range(1, n*n+1):
            matrix[i][j] = k
            visited[i][j] = 1
            di, dj = dirr[d]
            while(i+di < 0 or j+dj < 0 or i+di >= n or j+dj >= n or visited[i+di][j+dj]):
                d = (d+1) % 4
                di, dj = dirr[d]
                if(k == n*n):
                    break
            i, j = i+di, j+dj
        return matrix
