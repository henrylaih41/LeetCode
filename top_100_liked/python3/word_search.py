class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, found = len(board), len(board[0]), 0
        visited = [[0] * n for _ in range(m)]
        adj = [ [[] for _ in range(n)] for _ in range(m)]
        ### Contruct adj
        for i in range(m):
            for j in range(n):
                if(i-1 >= 0):
                    adj[i][j].append((i-1,j))
                if(i+1 < m):
                    adj[i][j].append((i+1,j))
                if(j-1 >= 0):
                    adj[i][j].append((i,j-1))
                if(j+1 < n):
                    adj[i][j].append((i,j+1))
                    
        for i in range(m):
            for j in range(n):
                if(board[i][j] == word[0]):
                    found = found or self.dfs(board, visited, i, j, word[1:], adj)
        return found
    
    def dfs(self, board, visited, i, j, word, adj):
        visited[i][j] = 1
        if(len(word) == 0):
            return 1 # found
        m, n, found = len(board), len(board[0]), 0
        
        for i_, j_ in adj[i][j]:
            if(not visited[i_][j_] and board[i_][j_] == word[0]):
                found = found or self.dfs(board, visited, i_, j_, word[1:], adj)
        visited[i][j] = 0     
        return found
