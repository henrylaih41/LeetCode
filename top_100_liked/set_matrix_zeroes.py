class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first, r, c = True, None, None
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(first and matrix[i][j] == 0):
                    r, c = i, j
                    first = False
                    for jj in range(n):
                        if(matrix[i][jj] == 0):
                            matrix[i][jj] = 1
                        else:
                            matrix[i][jj] = 0
                    for ii in range(m):
                        if(matrix[ii][j] == 0):
                            matrix[ii][j] = 1
                        else:
                            matrix[ii][j] = 0
                elif(matrix[i][j] == 0):
                    if(i != r and j != c):
                        matrix[r][j] = 1
                        matrix[i][c] = 1
                    
        if(r == None):
            return
        for j in range(n):
            if(matrix[r][j] == 1):
                for i in range(m):
                    matrix[i][j] = 0
        for i in range(m):
            if(matrix[i][c] == 1):
                for j in range(n):
                    matrix[i][j] = 0
        
