class Solution:
    ### Expand Center
    def AlongestPalindrome(self, s: str) -> str:
        maxx, start, end = 0, 0, 0

        for i in range(len(s)-1):
            # even palindrome center
            maxx = max(maxx, self.expandCenter(s, i, i+1))
            if(end - start + 1 < maxx):
                start = i - maxx//2 + 1
                end   = i + maxx//2
            if(i - 1 >= 0 and i + 1 < len(s)):
                # odd palindrome center
                maxx = max(maxx, self.expandCenter(s, i - 1, i + 1) + 1)
                if(end - start + 1 < maxx):
                    start = i - maxx//2
                    end   = i + maxx//2

        return s[start:end+1]

    def expandCenter(self, s, i, j):
        count = 0
        while(i >= 0 and j < len(s)):
            if(s[i] == s[j]):
                count += 2
                i -= 1
                j += 1
            else:
                break
        return count

    # DP
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # edge case
        if(n <= 1):
            return s
        # nxn matrix
        DP = [[0]*n for _ in range(n)]
        start, end = 0, 0
        # initial case
        for i in range(n):
            DP[i][i] = 1
        for i in range(n-1):
            if(s[i] == s[i+1]):
                DP[i][i+1] = 1
                if(end - start < 1):
                    start, end = i, i+1
        # constructing table
        for j in range(1, n):
            for i in range(0, j):
                if(DP[i+1][j-1] and s[i] == s[j]):
                    DP[i][j] = 1
                    if(end - start < j - i):
                        start, end = i, j
        return s[start:end+1]
