from typing import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursive_gen(n, 0)

    def recursive_gen(self, l, r):
        result = []
        ### base case
        if(not l and not r):
            return [""]

        if(l): # l > 0
            for s in self.recursive_gen(l-1, r+1):
                result.append('(' + s)
        if(r): # r > 0
            for s in self.recursive_gen(l, r-1):
                result.append(')' + s)

        return result
