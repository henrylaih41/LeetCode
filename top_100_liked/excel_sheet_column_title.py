class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = 26
        ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while(columnNumber):
            i = (columnNumber-1) % (base)
            result.append(ss[i])
            columnNumber -= (i+1)
            columnNumber //= base
        return "".join(reversed(result))
