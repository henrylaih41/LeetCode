class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        self.dp = [[0]*len(s) for _ in range(len(s))]
        self.track, self.result = [], []
        for i in range(len(s)):
            for j in range(len(s)):
                if(s[i:j+1] in wordDict):
                    self.dp[i][j] = 1
        self.backtrack(s, 0)
        ans = []
        for cand in self.result:
            ans.append(" ".join(cand))
        return ans
    def backtrack(self, s, head):
        if(head == len(s)):
            self.result.append(self.track.copy())
            return 
        for tail in range(head, len(s)):
            if(self.dp[head][tail]):
                self.track.append(s[head:tail+1])
                self.backtrack(s, tail+1)
                self.track.pop()
