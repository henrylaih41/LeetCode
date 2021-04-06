class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        visited = {}
        adj = {}
        for w in wordList:
            visited[w] = 0
        for w in wordList:
            adj[w] = []
            for i in range(len(w)):
                ss = w[:i] + "*" + w[i+1:]
                adj[w].append(ss)
                if(ss not in adj):
                    adj[ss] = []
                adj[ss].append(w)
        ### BFS
        q = [beginWord]
        visited[beginWord] = 1
        level = 1
        while(len(q) != 0):
            nq = []
            level += 1
            for w in q:
                for n in adj[w]:
                    for nn in adj[n]:
                        if(nn == endWord):
                            return level
                        if(not visited[nn]):
                            nq.append(nn)
                            visited[nn] = 1
            q = nq
        return 0
