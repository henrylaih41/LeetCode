class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        summ = 0
        for c in columnTitle:
            summ *= 26
            summ += (ord(c) - ord('A') + 1)
        return summ
