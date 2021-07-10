class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        self.dirr = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1,-1)]
        for i in range(self.m):
            for j in range(self.n):
                self.count(board, i, j)
        for i in range(self.m):
            for j in range(self.n):
                board[i][j] >>= 1
        
    def count(self, board, i, j):
        cc = 0
        for di, dj in self.dirr:
            if(i + di < self.m and i + di >= 0 and j + dj < self.n and j + dj >= 0):
                cc += board[i+di][j+dj] % 2
        if(cc < 2):
            pass
        elif(cc == 2):
            board[i][j] |= 2*(board[i][j] % 2)
        elif(cc == 3):
            board[i][j] |= 2
        else:
            pass
