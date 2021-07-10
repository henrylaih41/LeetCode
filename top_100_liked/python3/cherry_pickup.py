from collections import defaultdict
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid, n = grid, len(grid)
        dp = defaultdict(lambda: -math.inf)
        dp[(0, 0)] = grid[0][0]
        ### first half
        for level in range(2, n+1):
            ndp = defaultdict(lambda: -math.inf)
            for i in range(level):
                v1 = self.toCordValue(i, level-1, 0)
                if(v1 == -1):
                    continue
                for j in range(i, level):
                    v2 = self.toCordValue(j, level-1, 0)
                    if(v2 == -1):
                        continue
                    summ = v1 if (i == j) else v1 + v2
                    ndp[(i, j)] = max(dp[(i-1, j-1)], dp[(i-1, j)], dp[(i, j-1)], dp[(i, j)]) + summ
            dp = ndp  
​
        ### second half
        for level in range(n-1, 0, -1):
            ndp = defaultdict(lambda: -math.inf)
            for i in range(level):
                v1 = self.toCordValue(i, n-1, n-level)
                if(v1 == -1):
                    continue
                for j in range(i, level):
                    v2 = self.toCordValue(j, n-1, n-level)
                    if(v2 == -1):
                        continue
                    summ = v1 if (i == j) else v1 + v2
                    ndp[(i, j)] = max(dp[(i, j)], dp[(i, j+1)], dp[(i+1, j)], dp[(i+1, j+1)]) + summ
            dp = ndp
        return max(0, dp[(0,0)])
    
    def toCordValue(self, i, offset_x, offset_y):
        return self.grid[offset_x-i][offset_y+i]
    
