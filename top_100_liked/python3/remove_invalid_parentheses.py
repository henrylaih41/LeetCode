class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.l, self.r = self.getInvalid(s)
        self.result, self.sett = [], set()
        self.backtrack(s, 0, [], 0, 0, 0, 0)
        return self.result
    
    def backtrack(self, s, i, memo, cl, cr, l, r):
        if(l > self.l or r > self.r or cr > cl):
            return
        if(i == len(s)):
            if(cr == cl):
                ss = "".join(memo)
                if(ss not in self.sett):
                    self.result.append("".join(memo))
                    self.sett.add(ss)
            return 
        if(s[i] not in "()"):
            memo.append(s[i])
            self.backtrack(s, i+1, memo, cl, cr, l, r)
            memo.pop()
            return
        memo.append(s[i])
        if(s[i] == "("):
            self.backtrack(s, i+1, memo, cl+1, cr, l, r)
        else:
            self.backtrack(s, i+1, memo, cl, cr+1, l, r)
        memo.pop()
        
        if(s[i] == "("):
            self.backtrack(s, i+1, memo, cl, cr, l+1, r)
        else:
            self.backtrack(s, i+1, memo, cl, cr, l, r+1)
            
    def getInvalid(self, s):
        l, r, ir = 0, 0, 0
        for c in s:
            if(c not in "()"):
                continue
            if(c == "("):
                l += 1
            if(c == ")"):
                r += 1
            if(r > l):
                ir += 1
                r  -= 1
        return l - r, ir
