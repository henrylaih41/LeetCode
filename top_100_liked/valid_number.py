class Solution:
    def isNumber(self, s: str) -> bool:
        dotSeen, IntegerSeen, eSeen = 0, 0, 0
        for i, c in enumerate(s):
            if(not c.isdigit() and c not in "Ee.+-"):
                return False
            if(c.isdigit()):
                IntegerSeen = 1
            if(c in "+-"):
                if(i > 0 and s[i-1] not in "Ee"):
                    return False
            if(c in "Ee"):
                if(eSeen or not IntegerSeen):
                    return False
                eSeen = 1
                IntegerSeen = 0
            if(c == "."):
                if(dotSeen or eSeen):
                    return False
                dotSeen = 1
            
        return IntegerSeen
