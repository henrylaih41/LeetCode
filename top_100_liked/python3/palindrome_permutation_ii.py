from collections import defaultdict
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if(not self.canPermutePalindrome(s)):
            return []
        self.odd_char = ""
        self.result = set()
        mapp = defaultdict(lambda: 0)
        for c in s:
            mapp[c] += 1
        keys = list(mapp.keys())
        for k in keys:
            # only happen once
            if(mapp[k] % 2 == 1):
                mapp[k] -= 1
                self.odd_char = k
            mapp[k] //= 2
            if(mapp[k] == 0):
                del mapp[k]
        self.backtrack(mapp, [])
        return list(self.result)
        
        
        
    def backtrack(self, char_count, arr):
        if(len(char_count) == 0):
            s = "".join(arr)
            self.result.add(s + self.odd_char + s[::-1])
            return
        keys = list(char_count.keys())
        for k in keys:
            arr.append(k)
            char_count[k] -= 1
            if(char_count[k] == 0):
                del char_count[k]
            self.backtrack(char_count, arr)
            arr.pop()
            char_count[k] += 1
        
        
    def canPermutePalindrome(self, s: str) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        odd_count = 0
        for i in range(26):
