class Solution:
    def recursive_util(self, cand, target):
        result = []
        ### base case
        if(target == 0):
            return [[]]

        for idx, i in enumerate(cand):
            if(target - i < 0):
                break
            r = self.recursive_util(cand[idx:], target - i)
            for l in r:
                l.insert(0,i) #insert(0,i) would cause result to be ascending, and append(i) descending
                result.append(l)
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.recursive_util(candidates, target)

