class TrieNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isWord = None
    
    def inChild(self, c):
        return self.child[ord(c) - ord('a')]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    ### insert a word into Trie    
    def insert(self, s, pos):
        n, i = self.root, 0
        while(i < len(s)):
            idx = self.index(s[i])
            if(n.child[idx] != None):
                n = n.child[idx]
            else:
                nn = TrieNode()
                n.child[idx] = nn
                n = nn
            i += 1
        n.isWord = pos
        
    def index(self, c):
        return ord(c) - ord('a')
​
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m, self.n, t, self.maxx = len(board), len(board[0]), Trie(), 0
        m, n = self.m, self.n
        for i, w in enumerate(words):
            self.maxx = max(self.maxx, len(w))
            t.insert(w, i)
        self.visited = [[0]*n for _ in range(m)]
        self.result  = [0 for _ in range(len(words))]
        self.dirr = [(0,1), (1,0), (-1,0), (0,-1)]
        self.length  = 0
        for i in range(m):
            for j in range(n):
                node = t.root.inChild(board[i][j])
                if(node != None):
                    self.dfs(i, j, node, board, 1)
        
        ans = []
        for i in range(len(self.result)):
            if(self.result[i]):
                ans.append(words[i])
        return ans
    
    ### search only if unvisited and in TRIE
    def dfs(self, i, j, node, board, length):
        self.visited[i][j] = 1
        if(node.isWord != None):
