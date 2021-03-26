class UnionFind:
        def __init__(self, size, m, n):
            self.union = [i for i in range(size)]
            self.rank  = [0] * size
            self.alive = [0] * size
            ### set edge as alive
            for i in range(m):
                for j in range(n):
                    if(i == 0 or i == m-1 or j == 0 or j == n-1):
                        self.alive[i*n + j] = 1
            
        def find(self, idx):
            ### path compression
            while(self.union[idx] != idx):
                self.union[idx] = self.union[self.union[idx]]
                idx = self.union[idx]
                
            return idx
​
        def uunion(self, x, y):
            xp = self.find(x)
            yp = self.find(y)
            if(xp == yp):
                return 
           
            if(self.rank[xp] > self.rank[yp]):
                self.union[yp] = xp
                self.alive[xp] = self.alive[xp] or self.alive[yp]
            elif(self.rank[yp] > self.rank[xp]):
                self.union[xp] = yp
                self.alive[yp] = self.alive[xp] or self.alive[yp]
            else:
                self.union[xp] = yp
                self.alive[yp] = self.alive[yp] or self.alive[xp]
                self.rank[yp] += 1
​
class Solution:
        def solve(self, board: List[List[str]]) -> None:
            m, n = len(board), len(board[0])
            un = UnionFind(m*n, m, n)
            for i in range(m):
                for j in range(n):
                    if(j+1 < n and board[i][j] == board[i][j+1]):
                        un.uunion(n*i+j, n*i+j+1)
                    if(i+1 < m and board[i][j] == board[i+1][j]):
                        un.uunion(n*i+j, n*(i+1) + j)
​
