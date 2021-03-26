class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.d = {}
        prefix, count = 0, 0
        for n in nums:
            prefix += n
            if(prefix == k):
                count += 1
            if((prefix-k) in self.d):
                count += self.d[prefix - k]
            if(prefix not in self.d):
                self.d[prefix] = 1
            else:
                self.d[prefix] += 1
        return count
