class Solution:
    ### find the longest path between two leaf nodes
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if(len(edges) == 0):
            return [0]
        adj = [[] for i in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        self.edge, self.distance = None, 0
        self.visited = set()
        self.dfs(0, 0, adj)
        self.visited = set()
        self.result = None
        self.maxx = -math.inf
        self.solve(self.edge, [], adj)
        return list(set(self.result))
    def dfs(self, node, distance, adj):
        self.visited.add(node)
        if(distance > self.distance):
            self.edge = node
            self.distance = distance
        for neighbor in adj[node]:
            if(neighbor not in self.visited):
                self.dfs(neighbor, distance+1, adj)            
                
    def solve(self, node, path, adj):
        self.visited.add(node)
        path.append(node)
        if(len(path) > self.maxx):
            n = len(path)
            self.result = [path[n//2], path[(n+1)//2-1]]
            self.maxx = n
        for neighbor in adj[node]:
            if(neighbor not in self.visited):
                self.solve(neighbor, path, adj)
        path.pop()
        
