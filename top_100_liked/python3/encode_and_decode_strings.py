class Codec:
    def encode(self, strs: [str]) -> str:
        strings = []
        k = self.getMaxLen(strs)
        strings.append(chr(len(str(k))))
        for s in strs:
            strings.append(str(len(s)).rjust(len(str(k)), "0"))
            strings.append(s)
        return "".join(strings)
        """Encodes a list of strings to a single string.
        """
        
    def getMaxLen(self, strs):
        maxx = -math.inf
        for s in strs:
            maxx = max(maxx, len(s))
        return maxx
    
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        k = ord(s[0])
        i = 1
        while(i < len(s)):
            l = int(s[i:i+k])
            result.append(s[i+k:i+k+l])
            i = i+k+l
        return result
​
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
