class Solution:
    def __init__(self):
        self.flag = 1
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
        for n in range(numCourses):
            if(not visited[n]):
                self.dfs(n, adj, visited)
        return self.flag
    
    # 0 is unvisited, 1 is in process, 2 is done
    def dfs(self, i, adj, visited):
        visited[i] = 1 
        for j in adj[i]:
            if(not visited[j]):
                self.dfs(j, adj, visited)
            elif(visited[j] == 1):
                self.flag = 0
        visited[i] = 2
