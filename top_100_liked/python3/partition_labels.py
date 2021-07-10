class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ### turn into intervals
        d = {}
        for i, c in enumerate(S):
            if(c not in d):
                d[c] = [i, i] # start position
            d[c][1] = i # update end position
        intervals = []
        for key in d:
            intervals.append(d[key])
        #print(intervals)
        return self.solve(intervals)
    
    def solve(self, intervals):
        event, result = [], []
        for s, e in intervals:
            event.append((s, -1))
            event.append((e, 1))
        event.sort()
        #print(event)
        count, head = 0, 0
        for t, i in event:
            count -= i
            ### t must be an end time
            if(count == 0):
                result.append(t - head + 1)
                head = t+1
        return result
            
