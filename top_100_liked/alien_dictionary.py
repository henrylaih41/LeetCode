class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = [[] for _ in range(26)] # 26 alphabets
        visited = [0] * 26
        alphas = set()
        self.cycle = 0
        ### O(C) C = total characters
        for w in words:
            for c in w:
                alphas.add(ord(c)-ord('a'))
        ### Extract infomation 
        for i in range(len(words)-1):
            c1, c2 = self.findDiff(words, i, i+1)
            if(c1 and c2):
                i1, i2 = ord(c1) - ord('a'), ord(c2) - ord('a')
                adj[i2].append(i1)
            if(self.cycle):
                return ""
        self.result = []
        ### topology sort
        for i in alphas:
            if(not visited[i]):
                self.dfs(i, adj, visited)
            if(self.cycle):
                return ""
        return "".join(self.result)
    
    ### if there is cycle 
    def dfs(self, i, adj, visited):
        visited[i] = 1
        for n in adj[i]:
            if(self.cycle or visited[n] == 1):
                self.cycle = 1
                break
            if(not visited[n]):
                self.dfs(n, adj, visited)
        self.result.append(chr(i+ord('a')))
        visited[i] = 2
​
    ### O(longestWordLength)
    def findDiff(self, words, i, j):
