# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
​
class Solution:
    def findCelebrity(self, n: int) -> int:
        q = [i for i in range(n)]
        while(len(q) > 1):
            nq = []
            ### n//2 + n//4 + ... + 1 = bounded by n
            for i in range(0, len(q), 2):
                if(i+1 < len(q)):
                    if(knows(q[i], q[i+1])):
                        nq.append(q[i+1]) 
                    else:
                        nq.append(q[i])
            if(len(q) % 2):
                    nq.append(q[-1])
            q = nq
        if(len(q) == 0):
            return -1
        cand = q[0]
        
        ### check if cand is celebrity
        for i in range(n):
            if(i == cand):
                continue
            if(knows(cand, i)):
                return -1
            if(not knows(i, cand)):
                return -1
        return cand
