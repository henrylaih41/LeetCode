class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        i = 0
        ss = strs[0]
        while(i < len(ss)):
            for s in strs:
                if(i >= len(s) or ss[i] != s[i]):
                    return ss[:i]
            i += 1
            
        return ss
            
                
