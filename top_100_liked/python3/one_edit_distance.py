class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if(abs(len(s)-len(t)) > 1 or s == t):
            return False
        if(len(t) > len(s)):
            s, t = t, s
        for i in range(len(t)):
            if(s[i] != t[i]):
                if(len(s) > len(t)):
                    return (s[i+1:] == t[i:])
                else:
                    return s[i+1:] == t[i+1:]
        return True
