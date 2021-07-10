class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for c in tasks:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        maxx = -math.inf
        for key in d:
            maxx = max(d[key], maxx)
        count = 0
        for key in d:
            if(d[key] == maxx):
                count += 1
        
        return max(len(tasks), (n+1)*(maxx-1) + count)
