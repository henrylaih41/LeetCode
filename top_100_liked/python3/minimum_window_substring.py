class Solution:
    def minWindow(self, s: str, t: str) -> str:
        head, tail, minn, needed = 0, 0, len(s)+1, len(set(t))
        start, end = 0, 0
        d, need_dict = {}, {}
        for c in t:
            d[c] = 0
            if c not in need_dict:
                need_dict[c] = 1
            else:
                need_dict[c] += 1

        while(tail < len(s)):
            if(s[tail] in d):
                d[s[tail]] += 1
                if(d[s[tail]] == need_dict[s[tail]]):
                    needed -= 1
            tail += 1
            while(head < len(s) and (s[head] not in d or d[s[head]] > need_dict[s[head]])):
                if(s[head] in d):
                    d[s[head]] -= 1
                head += 1
            if(not needed and (tail - head < minn)):
                start, end = head, tail
                minn = end - start

        return s[start: end]
