class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.backtrack({}, set(), pattern, s, 0, 0)
    
    def backtrack(self, mapp, sett, pattern, s, i, j):
        if(i >= len(pattern) or j >= len(s)):
            if(i == len(pattern) and j == len(s)):
                return True
            return False
        ss = mapp.get(pattern[i], None)
        ### pattern mapped
        if(ss):
            ll = len(ss)
            if(ss == s[j:j+ll]):
                return self.backtrack(mapp, sett, pattern, s, i+1, j+ll)
            else:
                return False        
        ### pattern unmapped
        else:
            for l in range(j+1, len(s)+1):
                if(s[j:l] in sett):
                    continue
                sett.add(s[j:l])
                mapp[pattern[i]] = s[j:l]
                if(self.backtrack(mapp, sett, pattern, s, i+1, l)):
                    return True
                del mapp[pattern[i]]
                sett.remove(s[j:l])
            return False
                
