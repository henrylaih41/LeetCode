class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = {}
        ### O(L)
        for w in words:
            bit = 0
            for c in w:
                bit |= (1 << (ord(c) - ord("a")))
            bitmask[w] = bit
        s_words = sorted(words, key=lambda x : len(x))
        i, j = 0, len(s_words)-1
        maxx = 0
        while(i < j):
            for k in range(j-1, i-1, -1):
                if (not(bitmask[s_words[j]] & bitmask[s_words[k]])):
                    maxx = max(maxx, len(s_words[j])*len(s_words[k]))
                    i = k+1
                    break
            j -= 1
        return maxx
