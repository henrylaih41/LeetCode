class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        i = len(s) - 1
        while(i >= 0 and s[i] == ' '):
            i -= 1
        if(i == -1):
            return 0
        j = i
        while(i >= 0 and s[i] != " "):
            i -= 1
        
            
        return j - i
