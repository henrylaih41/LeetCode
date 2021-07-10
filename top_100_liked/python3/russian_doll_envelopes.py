class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        ### LIS on h, w sorted 
        tails = [-math.inf]
        for _, h in envelopes:
            i = self.search(tails, h)
            if(i == len(tails)):
                tails.append(h)
            else:
                tails[i] = h
        return len(tails)-1
    
    ### smallest i that tails[i] >= value
    def search(self, tails, value):
        l, r = 0, len(tails)
        while(l < r):
            mid = (l+r)//2
            if(tails[mid] >= value):
                r = mid
            else:
                l = mid + 1
        return l
