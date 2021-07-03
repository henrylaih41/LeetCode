class Solution:
    ### backtracking (TLE if no checking for len(s))
    def restoreIpAddresses(self, s: str) -> List[str]:
        if(len(s) > 12):
            return []
        self.result = []
        self.dfs([], 0, s)
        return self.result
    
    def dfs(self, valid, i, s):
        if(len(valid) == 4 and i == len(s)):
            self.result.append(".".join(valid))
        if(i >= len(s)):
            return
        ### at most three digtis
        ss = ""
        for j in range(i, len(s)):
            ss += s[j]
            if(int(ss) > 255):
                break
            valid.append(ss)
            self.dfs(valid, j+1, s)
            valid.pop()
            ### no leading zero
            if(ss == "0"):
                break
    
        
        
