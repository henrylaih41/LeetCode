class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort() # default key = 0
        result.append(intervals[0])

        for l in intervals[1:]:
            e1 = result[-1][1]
            if(l[0] <= e1):
                result[-1][1] = max(e1, l[1])
            else:
                result.append(l)

        return result
