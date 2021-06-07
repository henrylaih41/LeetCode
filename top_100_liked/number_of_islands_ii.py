        if(px == py):
            return
        ### every union decrease the number of island by one
        self.count -= 1
        if(self.rank[px] > self.rank[py]):
            self.parent[py] = px
        elif(self.rank[py] > self.rank[px]):
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px]  += 1
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DisjointSet(m*n)
        result, neighbor = [], [[0, 1], [1, 0], [-1, 0], [0,-1]]
        for x, y in positions:
            idx = n*x + y
            ds.add(idx)
            for dx, dy, in neighbor:
                x_, y_ = x + dx, y + dy
                if(x+dx < 0 or x+dx >= m or y+dy<0 or y+dy >= n):
                    continue
                ds.union(idx, n*x_ + y_)
            result.append(ds.count)
        return result
        
        
        
        
        
