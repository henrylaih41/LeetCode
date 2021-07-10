class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ### topology sort
        n, self.result = numCourses, []
        self.flag = 0
        adj = [[] for _ in range(n)]
        for i, j in prerequisites:
            adj[i].append(j)
        visited = [0 for _ in range(n)]
        
        for i in range(n):
            if(visited[i] == 0):
                self.dfs(i, adj, visited)
        
        if(self.flag):
            return []
        return self.result
    
    def dfs(self, i, adj, visited):
        visited[i] = 1 # gray
        for j in adj[i]:
            if(visited[j] == 0):
                self.dfs(j, adj, visited)
            ### cycle
            if(visited[j] == 1):
                self.flag = 1
                return
        self.result.append(i)
        visited[i] = 2
