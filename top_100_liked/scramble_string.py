from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.memo = defaultdict(lambda: dict())
    def isScramble(self, s1, s2):
        #if(self.unique(s1) and self.unique(s2)):
        #    return self.isScrambleForUnique(s1, s2)
        if(s2 in self.memo[s1]):
            return self.memo[s1][s2]
        if(len(s1) != len(s2)):
            return False
        if(len(s1) == 1):
            return s1[0] == s2[0]
        if(s1 == s2):
            return True
        for j in range(1, len(s1)):
            for s in range(2):
                if(s):
                    if(self.isScramble(s1[j:], s2[:len(s1)-j]) and self.isScramble(s1[:j], s2[len(s1)-j:])):
                        self.memo[s1][s2] = 1
                        return True
                else:
                    if(self.isScramble(s1[:j], s2[:j]) and self.isScramble(s1[j:], s2[j:])):
                        self.memo[s1][s2] = 1
                        return True
        self.memo[s1][s2] = 0
        return False
    def unique(self, s):
        d = {}
        for c in s:
            if(c in d):
                return False
            d[c] = 1
        return True
    ### only work if s1 s2 has no duplicate character
    def isScrambleForUnique(self, s1: str, s2: str) -> bool:
        if(len(s1) != len(s2)):
            return False
        if(len(s1) == 1):
            return s1[0] == s2[0]
        if(s1 == s2):
            return True
        not_possible_set = set()
        d = {}
        for i, c in enumerate(s2):
            d[c] = i
