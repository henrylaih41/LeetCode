class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.Done = 0
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.box = [set() for _ in range(9)]
        i_, j_ = None, None
        for i in range(9):
            for j in range(9):
                if(board[i][j] == "." and i_ == None):
                    i_, j_ = i, j
                else:
                    self.row[i].add(board[i][j])
                    self.col[j].add(board[i][j])
                    self.box[(i//3)*3 + j//3].add(board[i][j])
                    
        self.solve(board, i_*9 + j_)
        
    def solve(self, board, idx):
        if(idx > 80):
            self.Done = 1
            return
        i = idx // 9
        j = idx % 9
        
        if(board[i][j] != "."):
            self.solve(board, idx+1)
            return 
        
        for n in range(1, 10):
            if(not self.Done and self.Put(i, j, str(n))):
                board[i][j] = str(n)
                self.solve(board, idx+1)
                self.Remove(i, j, str(n))
                
        if(not self.Done):
            board[i][j] = "."
                
    ### return True if we success in putting, False if invalid move
    def Put(self, i, j, val):
        if(val in self.row[i]):
            return False
        if(val in self.col[j]):
            return False
        if(val in self.box[(i//3)*3 + j//3]):
            return False
        self.row[i].add(val)
        self.col[j].add(val)
        self.box[(i//3)*3 + j//3].add(val)
        return True
    
    def Remove(self, i, j, val):
        self.row[i].remove(val)
