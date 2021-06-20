from collections import defaultdict
class Solution:
    ### 1. simple O(n) time and space hash solution
    def findTheDifference(self, s: str, t: str) -> str:
        h = defaultdict(lambda: 0)
        for c in s:
            h[c] += 1
        for c in t:
            h[c] -= 1
            if(h[c] < 0):
                return c
        
