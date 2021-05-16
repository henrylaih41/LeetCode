class Solution:
    ### use recursive
    def permuteUnique(self, nums):
        result = set()
        if(len(nums) == 1):
            return [[nums[0]]]
        for l in self.permuteUnique(nums[1:]):
            for i in range(len(l)+1):
                nl = l.copy()
                nl.insert(i, nums[0])
                result.add(tuple(nl))
        return [list(l) for l in list(result)]
    
    def v1permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = self.getCount(nums)
        self.s = set()
        self.backtrace(counter, [], len(nums))
        return list(self.s)
    ### maybe we could use a linked list to accelerate
    def backtrace(self, counter, comb, k):
        for i in range(len(counter)):
            if(counter[i][1] <= 0):
                continue
            comb.append(counter[i][0])
            counter[i][1] -= 1
            if(len(comb) == k):
                self.s.add(tuple(comb))
            else:
                self.backtrace(counter, comb, k)
            comb.pop()
            counter[i][1] += 1
    
    def getCount(self, l):
        result = []
        d = {}
        for n in l:
            d[n] = d.get(n, 0) + 1
        for k in d.keys():
            result.append([k, d[k]])
        return sorted(result)
