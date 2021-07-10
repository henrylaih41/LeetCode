from collections import deque
class Node:
    def __init__(self, name, valid):
        self.visited = 0
        self.adj = []
        self.name = name
        self.isValid = valid
        self.depth = None
        
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if(endWord not in wordList):
            return []
        nodes = {}
        wordList.append(beginWord)
        for w in wordList:
            n = Node(w, 1)
            nodes[w] = n
            for i in range(len(w)):
                neigh = w[:i] + "*" + w[i+1:]
                if(neigh not in nodes):
                    neigh_n = Node(neigh, 0)
                    nodes[neigh] = neigh_n
                else:
                    neigh_n = nodes[neigh]
                n.adj.append(neigh_n)
                neigh_n.adj.append(n)
        ### BFS
        q = deque([nodes[beginWord]])
        nodes[beginWord].visited = 1
        nodes[beginWord].depth = 0
        while(len(q)):
            n = q.popleft()
            for adj in n.adj:
                if(not adj.visited):
                    q.append(adj)
                    adj.visited = 1
                    adj.depth = n.depth+1
                if(adj.name == endWord):
                    q = []
                    break
        ### DFS
        self.result = []
        self.dfs([], nodes[endWord])
        return self.result
    
    def dfs(self, path, node):
        if(node.depth == 0):
            path.append(node.name)
            self.result.append(list(reversed(path)))
            path.pop()
            return 
        for adj in node.adj:
            if(adj.depth != None and adj.depth < node.depth):
                if(node.isValid):
                    path.append(node.name)
                self.dfs(path, adj)
                if(node.isValid):
                    path.pop()
        
            
