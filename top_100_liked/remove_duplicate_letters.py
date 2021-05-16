class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d, seen = {}, set()
        for c in s:
            d[c] = d.get(c, 0) + 1
        ss = []
        for c in s:
            d[c] -= 1
            if(c in seen):
                continue
            while(len(ss) > 0 and ord(c) < ord(ss[-1]) and d[ss[-1]] > 0):
                seen.remove(ss.pop())
            ss.append(c)
            seen.add(c)
            
        return "".join(ss)
        
