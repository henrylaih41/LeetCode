class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank   = [0] * size
        self.count  = size    
    def find(self, x):
        ### find with path compression
        while(x != self.parent[x]):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if(px == py):
            return
        self.count -= 1
        if(self.rank[px] > self.rank[py]):
            self.parent[py] = px
        elif(self.rank[py] > self.rank[px]):
            self.parent[px] = py
        ### same rank
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = DisjointSet(n)
        for x, y in edges:
            disjointSet.union(x, y)
        return disjointSet.count
