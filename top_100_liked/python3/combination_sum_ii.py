class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.prefix = [0] * len(candidates)
        summ = 0
        for i in range(len(candidates)-1, -1, -1):
            summ += candidates[i]
            self.prefix[i] = summ
        return list(set(self.solve(candidates, 0, target)))
    
    def solve(self, cand, start, target):
        if(start >= len(cand) or cand[start] > target or self.prefix[start] < target):
            return []
        if(cand[start] == target):
            return [(cand[start],)]
        result = []
        for l in self.solve(cand, start+1, target-cand[start]):
            result.append((cand[start],) + l)
        for l in self.solve(cand, start+1, target):
            result.append(l)
        return result
    
