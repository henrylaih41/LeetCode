class TicTacToe:
​
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [[n, -1] for _ in range(n)]
        self.cols = [[n, -1] for _ in range(n)]
        self.diag = [[n, -1], [n, -1]] # 0 for normal, 1 for anti
        
    def move(self, row: int, col: int, player: int) -> int:
        r1, r2 = self.check(self.rows, row, player), self.check(self.cols, col, player)
        r3, r4 = 0, 0
        if(row == col):
            r3 = self.check(self.diag, 0, player)
        if(row + col == len(self.rows)-1):
            r4 = self.check(self.diag, 1, player)
        
        return max(r1,r2,r3,r4)
    def check(self, arr, i, player):
        arr[i][0] -= 1
        
        if(arr[i][1] == -1):
            arr[i][1] = player
        elif(arr[i][1] != player):
            arr[i][1] = 0
        
        if(arr[i][0] == 0 and arr[i][1] != 0):
            return player
        return 0
        
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
​
​
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
