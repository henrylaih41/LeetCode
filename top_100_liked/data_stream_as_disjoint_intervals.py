class SummaryRanges:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        
    ### O(len(intervals))
    def addNum(self, val: int) -> None:
        if(len(self.intervals) == 0):
            self.intervals.append([val, val])
            return
        
        flag, left = 1, -math.inf
        for i, interval in enumerate(self.intervals):
            for point in interval:
                right = point
                if(left == val or right == val):
                    return 
                elif(left < val and right > val):
                    if(flag):
                        ### merge case
                        if(val == left+1 and val == right -1):
                            self.intervals[i-1][1] = self.intervals[i][1]
                            self.intervals.pop(i)
                        elif(val == left+1):
                            self.intervals[i-1][1] = val
                        elif(val == right-1):
                            self.intervals[i][0] = val
                        else:
                            self.intervals.insert(i, [val, val])
                    ### val in one of the existing intervals
                    return
​
                else:
                    left = point
                    flag = not flag
        if(val == self.intervals[-1][1] + 1):
            self.intervals[-1][1] = val
        else:
            self.intervals.append([val, val])
        
​
    def getIntervals(self) -> List[List[int]]:
        return self.intervals
​
​
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
