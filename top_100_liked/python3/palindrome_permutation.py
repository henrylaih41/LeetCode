class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        odd_count = 0
        for i in range(26):
            if(counts[i] % 2):
                odd_count += 1
                if(odd_count > 1):
                    return False 
        return True
