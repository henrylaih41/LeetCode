class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank   = [0] * n
    
    def find(self, x):
        ### path compression
        while(self.parent[x] != x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def Union(self, x, y):
        x, y = self.find(x), self.find(y)
        if(x == y):
            return 1
        if(self.rank[x] > self.rank[y]):
            self.parent[y] = x
        elif(self.rank[y] > self.rank[x]):
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1
        return 0
    
class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ### tree only has n-1 edges
        if(len(edges) != n-1):
            return False
        D = DisjointSet(n)
