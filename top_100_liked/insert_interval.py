class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, merge = [], []
        s, e = newInterval
        ### find start
        i = 0
        while(i < len(intervals)):
            if(s > intervals[i][1]):
                result.append(intervals[i])
            else:
                merge.append(min(s, intervals[i][0]))
                break
            i += 1
            
        while(i < len(intervals)):
            if(e <= intervals[i][1]):
                if(intervals[i][0] > e):
                    merge.append(e)
                else:
                    merge.append(intervals[i][1])
                    i += 1
                result.append(merge)
                break
            i += 1
            
        while(i < len(intervals)):
            result.append(intervals[i])
            i += 1
        if(len(merge) == 0):
            result.append(newInterval)
        if(len(merge) == 1):
            merge.append(e)
            result.append(merge)
            
        return result
