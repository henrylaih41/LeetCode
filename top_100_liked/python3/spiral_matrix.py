class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.m, self.n = len(matrix), len(matrix[0])
        self.visited = [[0] * self.n for _ in range(self.m)]
        self.rotate_matrix = [[0, -1], [1, 0]]
        self.result = []
        self.dfs(matrix, 0, 0, [0, 1])
        return self.result
    
    def dfs(self, matrix, i, j, dirr):
        self.result.append(matrix[i][j])
        self.visited[i][j] = 1
        for _ in range(2):
            di, dj = dirr
            if(self.check(i+di, j+dj)):
                self.dfs(matrix, i+di, j+dj, dirr)
                return
            else:
                dirr = self.rotate(dirr)
                #print(dirr)
    def check(self, i, j):
        if(i >= self.m or j >= self.n or i < 0 or j < 0):
            return False
        if(self.visited[i][j]):
            return False
        return True
    
    def rotate(self, dirr):
        new = [0, 0]
        new[0] = dirr[0] * self.rotate_matrix[0][0] + dirr[1] * self.rotate_matrix[1][0]
        new[1] = dirr[0] * self.rotate_matrix[0][1] + dirr[1] * self.rotate_matrix[1][1]
        
        return new
