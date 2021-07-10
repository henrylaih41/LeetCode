class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        DP = [[0] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            DP[0][i] = i
        for i in range(m+1):
            DP[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                minn = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
                if(word1[i-1] == word2[j-1]):
                    minn = min(DP[i-1][j-1], minn)
                DP[i][j] = minn

        return DP[m][n]
