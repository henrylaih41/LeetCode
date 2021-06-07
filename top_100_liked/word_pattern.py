class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split(" ")
        if(len(tokens) != len(pattern)):
            return False
        mapp = {}
        s    = set()
        for k in range(len(pattern)):
            if(tokens[k] not in mapp):
                if(pattern[k] not in s):
                    mapp[tokens[k]] = pattern[k]
                    s.add(pattern[k])
                else:
                    return False
            elif(mapp[tokens[k]] != pattern[k]):
                return False
        return True
                
