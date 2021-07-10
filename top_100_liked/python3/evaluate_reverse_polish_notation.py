import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def myDiv(a, b):
            return math.trunc(a/b)
        ops = {
            "*" : operator.mul,
            "+" : operator.add,
            "-" : operator.sub,
            "/" : myDiv
        }
        s, sops = [], set("*+-/") 
        for token in tokens:
            if(token in sops): 
                r, l = s.pop(), s.pop()
                s.append(ops[token](l, r))
            else:
                s.append(int(token))
        return s[0]
