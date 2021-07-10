from collections import deque
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if(word1 == word2):
            q, minn = deque(), math.inf
            for i, w in enumerate(wordsDict):
                if(w == word1):
                    q.append(i)
                if(len(q) == 2):
                    minn = min(minn, q[1] - q[0])
                    q.popleft()
            return minn
        else:
            j, k, minn = math.inf, math.inf, math.inf
            for i in range(len(wordsDict)):
                if(wordsDict[i] == word1):
                    j = i
                    minn = min(minn, abs(j - k))
                if(wordsDict[i] == word2):
                    k = i
                    minn = min(minn, abs(j - k))
            return minn
