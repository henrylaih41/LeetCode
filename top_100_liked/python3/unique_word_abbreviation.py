class ValidWordAbbr:
​
    def __init__(self, dictionary: List[str]):
        self.d = defaultdict(lambda: 0)
        self.s = set()
        for w in dictionary:
            if(w in self.s):
                continue
            self.s.add(w)
            if(len(w) <= 2):
                key = w
            else:
                key = w[0] + str(len(w)-2) + w[-1]
            self.d[key] += 1
        
    def isUnique(self, word: str) -> bool:
        if(len(word) <= 2):
            key = word
        else:
            key = word[0] + str(len(word)-2) + word[-1]
        if(self.d[key] == 0):
            return True
        if(self.d[key] == 1 and word in self.s):
            return True
        return False
​
​
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
