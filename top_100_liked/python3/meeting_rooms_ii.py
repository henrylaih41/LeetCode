import functools
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))
        events.sort()
        count, maxx = 0, 0
        for t, c in events:
            count += c
            maxx = max(maxx, count)
        
        return maxx
