class Solution:
    def maxPoints(self, points):
        maxx = 1
        for i in range(len(points)):
            mapp = {}
            for j in range(len(points)):
                if(i == j):
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                a, d = y1 - y2, x1 - x2
                ### two special line x = k, y = k
                if(d == 0):
                    k = x1
                elif(a == 0):
                    k = (0,1)
                else:
                    g = gcd(a, d)
                    k = (a//g, d//g)
                if(k not in mapp):
                    mapp[k] = 2
                    maxx = max(maxx, 2)
                else:
                    mapp[k] += 1
                    maxx = max(maxx, mapp[k])
        return maxx
    
    def v1maxPoints(self, points: List[List[int]]) -> int:
        mapp = {}
        maxx = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if(i == j):
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
