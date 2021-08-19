import functools 
from collections import defaultdict
class Solution:
    ### O(n)
    def minimumLengthEncoding(self, words: List[str]) -> int:
        Trie = lambda : defaultdict(Trie)
        trie = Trie();
        for word in words:
            reduce(dict.__getitem__, word[::-1], trie)
        self.result = ""
        self.printTrie(trie, [])
        return len(self.result)
    
    def printTrie(self, trie, s):
        if(len(trie.keys()) == 0):
            self.result += ("".join(s) + "#")
        for k in trie.keys():
            s.append(k)
            self.printTrie(trie[k], s)
            s.pop()
