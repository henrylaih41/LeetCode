class Node:
    def __init__(self):
        self.isEnd = 0
        self.children = [None] * 26 # number of lower case English letter
        
class Trie:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def toIndex(self, c):
        return ord(c) - ord('a')
​
    def insert(self, word: str) -> None:
        if(len(word) == 0):
            return
        """
        Inserts a word into the trie.
        """
        node, i = self.root, 0
        while(i < len(word)):
            index = self.toIndex(word[i])
            if(node.children[index] == None):
                node.children[index] = Node()
            node = node.children[index]
            i += 1
        node.isEnd = 1
        
    def search(self, word):
        return self._search(word, 0)
​
    def _search(self, word, prefix) -> bool:
        node, i = self.root, 0
        index = self.toIndex(word[i])
        while(i < len(word)):
            index = self.toIndex(word[i])
            if(node.children[index]):
                node = node.children[index]
                i += 1
                continue
            break
        if(i == len(word) and (prefix or node.isEnd)):
