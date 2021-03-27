class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return "1"
        result = ""
        ss = self.countAndSay(n-1)
        prev, count = None, 0
        for c in ss:
            if(prev != c):
                if(prev != None):
                    result += str(count)
                    result += prev
                prev = c
                count = 1
            else:
                count += 1
        result += str(count)
        result += prev
        return result
