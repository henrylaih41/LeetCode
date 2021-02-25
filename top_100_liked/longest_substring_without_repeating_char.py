class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if(len(s) <= 1):
            return len(s)

        head, maxx, mapp = 0, 0, {}
        for i, c in enumerate(s):
            if(c in mapp and mapp[c] >= head):
                # c in sliding window
                head = mapp[c] + 1
            mapp[c] = i
            maxx = max(maxx, i - head + 1)
        return maxx
