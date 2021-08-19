class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapp = {"6" : "9",
                "9" : "6",
                "1" : "1",
                "8" : "8",
                "0" : "0"}
        
        s = ""
        for c in num[::-1]:
            if(c not in mapp):
                return False
            s += mapp[c]
        print(s)
        return (s == num)
