class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle == ""):
            return 0
        return self.KMP(haystack, needle)
    def KMP(self, s, p):
        i, j = 0, 0
        lps = self.lps(p)
        while(i < len(s)):
            if(s[i] == p[j]):
                i += 1
                j += 1
            elif(j != 0):
                j = lps[j-1]
            else:
                i += 1
            
            if(j == len(p)):
                ### if all we append
                ### result.append(i-j)
                ### j = lps[j-1]
                ### here we just return the first index
                return i - j
        return -1
        
    ### return the lps array, lps[i] means the length of the longest prefix match of p to p[i]
    def lps(self, p):
        result = [0] * len(p)
        i, j = 1, 0
        ### lps[0] is always 0
        while(i < len(p)):
            if(p[j] == p[i]):
                result[i] = j + 1 # result stores the length of match
                j += 1
                i += 1
            elif(j != 0):
                j = result[j-1]  # tricky part
            else:
                result[i] = 0
                i += 1
                
        return result
        
