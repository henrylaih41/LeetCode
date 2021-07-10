class WordDistance:
​
    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(lambda: [])
        for i, w in enumerate(wordsDict):
            self.d[w].append(i)
    
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.d[word1], self.d[word2]
        p1, p2, minn = 0, 0, math.inf
        while(p1 < len(l1) and p2 < len(l2)):
            minn = min(abs(l1[p1] - l2[p2]), minn)
            if(l1[p1] <= l2[p2]):
                p1 += 1
            else:
                p2 += 1
        return minn
​
​
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
