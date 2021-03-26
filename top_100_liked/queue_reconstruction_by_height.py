class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def cmp(x):
            return (-x[0], x[1])
        
        people.sort(key=cmp)
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
        
    def tooslowImplementaion(self):
        people.sort()
        n = len(people)
        queue = [None] * n
        mapp = [i for i in range(n)]
        prev = people[0][0]
        occupied = []
        for i in range(n):
            ### new round
            p = people[i]
            if(prev != p[0]):
                nmapp = []
                for i in mapp:
                    if(i not in occupied):
                        nmapp.append(i)
                mapp = nmapp
                prev = p[0]
            queue[mapp[p[1]]] = p
            occupied.append(mapp[p[1]])
​
        return queue
