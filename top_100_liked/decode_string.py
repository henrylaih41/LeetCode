class Solution:
    def decodeString(self, s: str) -> str:
        result = [] # we use join on result to get final string
        tokens = self.mysplit(s)
        print(tokens)
        for token in tokens:
            if(token == ""):
                continue
            if(self.hasDigit(token)):
                ss, rp, token = self.getInt(token)
                result.append(ss)
                s = self.decodeString(token)
                for _ in range(rp):
                    result.append(s)
            else:
                result.append(token)
                
        return "".join(result)
    
    def getInt(self, token):
        i = 0
        ### find the first digit
        while(not token[i].isdigit()):
            i += 1
        ### everything in front of first digit is strings
        ss = token[:i]
        token = token[i:]
        ### parsing
        i = 1
        while(True):
            if(token[:i].isdigit()):
                i += 1
            else:
                i -= 1
                break
        return ss, int(token[:i]), token[i+1:] # remove the "[" trailing after the int
        
    def mysplit(self, s):
