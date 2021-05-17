class Solution:
    def shortestPalindrome(self, s: str) -> str:
        func = self.kmp_func(s)
        i, j, rs = 0, 0, s[::-1]
        while(i < len(rs)):
            if(rs[i] == s[j]):
                j += 1
                i += 1
            elif(j):
                j = func[j-1] ### this is j-1 not j!!!
            else:
                i += 1
        # return s[-1:j-1:-1] + s 
        return rs[:len(s)-j] + s
    def kmp_func(self, s):
        func = [0] # the first one is always zero
        i, j = 1, 0
        while(i < len(s)):
            if(s[i] == s[j]):
                j += 1
                i += 1
                func.append(j)
            elif(j):
                j = func[j-1] ### this is j-1 not j!!!
            else:
                func.append(j) # j == 0
                i += 1
        return func
