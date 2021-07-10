class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        head = -1
        d = [0] * 26
        d_limit = [0] * 26
        for c in p:
            idx = self.index(c)
            d_limit[idx] += 1   
        #print(d_limit)
        count = len(p)
        result = []
        for i in range(len(s)):
            ### clear everything
            if(s[i] not in p):
                d = [0] * 26
                count = len(p)
            else:
                if(count == len(p)):
                    head = i
                idx = self.index(s[i])
                d[idx] += 1
                count -= 1
                while(d[idx] > d_limit[idx]):
                    d[self.index(s[head])] -= 1
                    count += 1
                    head += 1
                if(count == 0):
                    result.append(head)
        return result
    
    def index(self, c):
        return ord(c) - ord('a')
