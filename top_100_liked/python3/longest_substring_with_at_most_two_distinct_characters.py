from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        head, tail, maxx, count = 0, 0, 0, 0
        while(tail < len(s)):
            while(count == 2 and d[s[tail]] == 0):
                ### s[head] must be in dictionary, so d[s[head]] > 0
                d[s[head]] -= 1
                ### count maintains how many non-zero value in d
                if(d[s[head]] == 0):
                    count -= 1
                head += 1
            if(d[s[tail]] == 0):
                count += 1
            d[s[tail]] += 1
            tail += 1
            maxx = max(maxx, tail - head)
        return maxx
