class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        self.row = [0] * n
        self.col = [0] * n
        self.ldiag = [0] * (2*n-1)
        self.rdiag = [0] * (2*n-1)
        self.result = [] 
        self.backtrace(board, 0, n, n)
        return self.result
    
    def backtrace(self, board, idx, n, k):
        if(k == 0):
            self.addResult(board, n)
            return
        if(idx >= n*n):
            return
        i = idx // n
        j = idx % n
        ### put on board[i][j]
        if(self.put(board, i, j, n)):
            self.backtrace(board, idx+1, n, k-1)
            self.remove(board, i, j, n)
            
        ### skip board[i][j]
        self.backtrace(board, idx+1, n, k)
            
    def put(self, board, i, j, n):
        if(self.row[i] or self.col[j] or self.ldiag[(i+j)] or self.rdiag[i-j+n-1]):
            return False
        else:
            self.row[i] = 1
            self.col[j] = 1
            self.ldiag[(i+j)] = 1
            self.rdiag[i-j+n-1] = 1
            board[i][j] = "Q"
            return True
           
    def remove(self, board, i, j, n):
        board[i][j] = "."
        self.row[i] = 0
        self.col[j] = 0
        self.ldiag[(i+j)] = 0
        self.rdiag[i-j+n-1] = 0
           
    def addResult(self, board, n):
        self.result.append(["".join(board[i]) for i in range(n)])
