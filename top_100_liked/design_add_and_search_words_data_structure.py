from collections import deque
class TRIE_node:
    def __init__(self):
        self.child = {}
        self.isWord = 0
        
class WordDictionary:
    ### First thought: TRIE, do dfs on all child if we see "."
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TRIE_node()
​
    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            idx = word[i]
            child = node.child.get(idx, None)
            if(child == None):
                child = TRIE_node()
                node.child[idx] = child
            node = child
        node.isWord = 1
    
    def search(self, word: str) -> bool:
        #return self.recur_search(self.root, word, 0)
        return self.bfs(deque([(self.root, 0)]), word)
    
    def recur_search(self, node, word, i):
        if(i == len(word)):
            return node.isWord
        
        if(word[i] == "."):
            for j in node.child.keys():
                if(self.recur_search(node.child[j], word, i+1)):
                    return True
            return False
        
        idx = word[i]
        if(node.child.get(idx, None)):
            return self.recur_search(node.child[idx], word, i+1)
        else:
            return False
    
    def bfs(self, q, word):
        while(len(q)):
            node, i = q.popleft()
            if(i == len(word) and node.isWord):
                return True
            elif(i < len(word) and word[i] == "."):
                for k in node.child.keys():
                    q.append((node.child[k], i+1))
            elif(i < len(word) and node.child.get(word[i], None)):
                q.append((node.child[word[i]], i+1))
