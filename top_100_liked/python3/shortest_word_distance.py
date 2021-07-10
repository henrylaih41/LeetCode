class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i, j = math.inf, math.inf 
        minn = math.inf
        for k in range(len(wordsDict)):
            if(wordsDict[k] == word1):
                i = k
                minn = min(minn, abs(i - j))
            if(wordsDict[k] == word2):
                j = k
                minn = min(minn, abs(i - j))
        return minn
                
