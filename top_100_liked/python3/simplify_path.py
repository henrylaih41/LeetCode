class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        s = [] # "" is the root
        for token in tokens:
            if(token == ""):
                continue
            elif(token[0] == "." and len(token) < 3):
                i = len(token) - 1
                while(i and len(s)):
                    s.pop()
                    i -= 1
            else:
                s.append(token)
        return "/" + "/".join(s)
            
