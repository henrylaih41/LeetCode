class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(cost) > sum(gas)):
            return -1
        self.start, self.end, i = -1, -1, 0
        while(i < len(gas)):
            if(gas[i] >= cost[i]):
                break
            i += 1
        self.start, self.end = i, i
        summ = gas[i] - cost[i]
        i = (i + 1) % len(gas)
        while(i != self.end):
            if(self.start == -1 and gas[i] - cost[i] >= 0):
                self.start = i
            summ += (gas[i] - cost[i])
            if(summ < 0):
                self.start, summ = -1, 0
            i = (i + 1) % len(gas)
                
        return self.start
                
                
