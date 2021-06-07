class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ### citations[n-i] >= i and citation[n-i-1] <= i 1 <= i <= n-1
        l, r = 0, len(citations)
        while(l < r):
            i = (l+r) // 2
            if(i == 0):
                return 0 if citations[-1] == 0 else len(citations)
            if(citations[len(citations)-i] >= i):
                if(citations[len(citations)-i-1] > i):
                    l = i + 1
                else:
                    return i
            else:
                r = i
        return l
        
