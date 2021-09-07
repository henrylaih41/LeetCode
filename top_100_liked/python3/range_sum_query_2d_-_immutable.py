class NumMatrix:
​
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix_2D = [[0] * self.n for _ in range(self.m)]
        for j in range(self.n):
            for i in range(self.m):
                matrix_1 = self.prefix_2D[i-1][j] if i - 1 >= 0 else 0
                matrix_2 = self.prefix_2D[i][j-1] if j - 1 >= 0 else 0
                matrix_3 = self.prefix_2D[i-1][j-1] if ((i-1) >= 0 and (j-1) >= 0) else 0
                self.prefix_2D[i][j] = matrix[i][j] + matrix_1 + matrix_2 - matrix_3
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix_1 = self.prefix_2D[row1-1][col2] if(row1-1 >= 0 and col2 >= 0) else 0
        matrix_2 = self.prefix_2D[row2][col1-1] if(row2 >= 0 and col1-1 >= 0) else 0
        matrix_3 = self.prefix_2D[row1-1][col1-1] if(row1-1 >= 0 and col1-1 >= 0) else 0
        #print(self.prefix_2D[row2-1][col2-1], matrix_1, matrix_2, matrix_3)
        return self.prefix_2D[row2][col2] - matrix_1 - matrix_2 + matrix_3
​
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
