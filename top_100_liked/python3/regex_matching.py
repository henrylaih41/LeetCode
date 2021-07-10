from typing import *
class Solution:
    ### recursive
    def RisMatch(self, s: str, p: str) -> bool:
        # base case
        if(len(p) == 0):
            return not len(s)

        first_match = len(s) and (s[0] == p[0] or p[0] == '.')

        if(len(p) >= 2 and p[1] == "*"):
                    return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return first_match and self.isMatch(s[1:], p[1:])

    ### recursive + DP
    def isMatch(self, s: str, p: str) -> bool:
        DP = [[-1] * (len(p) + 1) for _ in range(len(s) + 1)]
        ### init condition
        DP[len(s)][len(p)] = 1 # true if s = "" p = ""
        for i in range(len(s)):
            DP[i][len(p)] = 0  # false if p = "" s != ""

        return self.match_DP(s, p, 0, 0, DP)

    def match_DP(self, s, p, i, j, DP):
        print(i, j, s, p, DP[i][j])
        # DP condition (base case handled)
        if(DP[i][j] != -1):
            return DP[i][j]

        # s might be ""
        first_match = len(s) and (s[0] == p[0] or p[0] == '.')

        if(len(p) >= 2 and p[1] == "*"):
            DP[i][j] = (first_match and self.match_DP(s[1:], p, i+1, j, DP)) or self.match_DP(s, p[2:], i, j+2, DP)
        else:
            DP[i][j] =  first_match and self.match_DP(s[1:], p[1:], i+1, j+1, DP)

        return DP[i][j]
