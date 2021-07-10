class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        head, count, maxx = 0, 0, 0
        d = {}
        
        for i, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            if(d[c] == 1):
                count += 1
            while(count > k):
                d[s[head]] -= 1
                if(d[s[head]] == 0):
                    count -= 1
                head += 1
            maxx = max(maxx, i-head+1)
        return maxx
            
