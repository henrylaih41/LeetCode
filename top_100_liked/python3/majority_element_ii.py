class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.generalizedMajorityElement(nums, 2)
        
    def generalizedMajorityElement(self, nums, k):
        if(len(nums) < k):
            return nums[:]        
        ### init candidate
        candidate = [[None, 0] for _ in range(k)]
        
        ### find candidate O(nk)
        for n in nums:
            zero = None
            found = False
            for i in range(len(candidate)):
                if(candidate[i][0] == n):
                    candidate[i][1] += 1
                    found = True
                    break
                if(candidate[i][1] == 0):
                    zero = i
            if(found):
                continue
            if(zero != None):
                candidate[zero][0] = n
                candidate[zero][1] = 1
            else:
                for i in range(len(candidate)):
                    candidate[i][1] -= 1
                    
        ### verify candidate O(nk)
        result = set()
        for cand, _ in candidate:
            count = 0
            for i in range(len(nums)):
                if(nums[i] == cand):
                    count += 1
            if(count > (len(nums) // (k+1))):
                result.add(cand)
        return list(result)
