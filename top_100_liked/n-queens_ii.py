class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        self.dfs([], [], [], n)
        return self.cnt
    def dfs(self, col, rd, ld, n):
        if(len(col) == n):
            self.cnt += 1
        i = len(col)
        for j in range(n):
            if(j not in col and i-j not in rd and i+j not in ld):
                self.dfs(col + [j], rd+[i-j], ld+[i+j], n)
        
