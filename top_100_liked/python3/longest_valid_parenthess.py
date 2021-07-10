class Solution:
    # DP
    def longestValidParentheses(self, s: str) -> int:
        DP = [0] * len(s)

        for i in range(1, len(s)):
            if(s[i] == '('):
                continue
            elif(s[i] == ')'):
                if(s[i-1] == '('):
                    DP[i] = 2 + (0 if (i-2) < 0 else DP[i-2])
                elif(s[i-1] == ')' and DP[i-1] != 0):
                    if(i - DP[i-1] - 1 >= 0 and s[i-DP[i-1]-1] == '('):
                        DP[i] = DP[i-1] + 2 + (0 if i-DP[i-1]-2 < 0 else DP[i-DP[i-1]-2])

        maxx = 0
        for i in range(len(s)):
            print(DP[i])
            maxx = max(DP[i], maxx)
        return maxx

    def SlongestValidParentheses(self, s: str) -> int:
        # total 8 case
        # 1: ) ... (
        # 2: ( ... (
        # 3: ) ... )
        # 4: ... )
        # 5: ... (
        # 6: ) ...
        # 7: ( ...
        # 8: ...
        # ... is a valid substring
        # left scan can find case 1, 3, 4, 5, 6, 8
        # right scan can find case 1, 2, 5, 6, 7, 8
        # so all case can be found
        n = len(s)

        # left scan
        l, r, maxx = 0, 0, 0
        for i in range(n):
            if(s[i] == '('):
                l += 1
            elif(s[i] == ')'):
                r += 1
            if(l == r):
                maxx = max(maxx, r*2)
            if(r > l):
                l, r = 0, 0
        l, r = 0, 0
        for i in range(n-1, -1, -1):
            if(s[i] == '('):
                l += 1
            elif(s[i] == ')'):
                r += 1
            if(l == r):
                maxx = max(maxx, r*2)
            if(l > r):
                l, r = 0, 0
        return maxx
