class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxx = 0
        for i in range(1, 27):
            maxx = max(self.check_N_Uniques(s, i, k), maxx)
        return maxx
    
    def check_N_Uniques(self, s, n, k):
        maxx, head = 0, 0
        cnt, u, d = 0, 0, {}
        for tail in range(len(s)):
            if(d.get(s[tail], 0) == 0):
                d[s[tail]] = 1
                u += 1
                while(u > n):
                    if(d[s[head]] == k):
                        cnt -= 1
                    d[s[head]] -= 1
                    if(d[s[head]] == 0):
                        u -= 1
                    head += 1
            else:
                d[s[tail]] += 1
            
            if(d[s[tail]] == k):
                cnt += 1
            if(cnt == n):
                maxx = max(maxx, tail-head+1)
        
        return maxx
