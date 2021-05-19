class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.encode(s) == self.encode(t)
    
    def encode(self, s):
        d, count = {}, 0
        result = []
        for c in s:
            if(d.get(c, None) == None):
                d[c] = count
                count += 1
            result.append(d[c])
        return result
​
