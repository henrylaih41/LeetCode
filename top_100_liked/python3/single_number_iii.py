class Solution:
    ### first we know how to do this when there is only one element that appeared once
    ### so now we transform this problem into that problem.
    ### let x, y be the two element that appeared only once
    ### we know that x, y must have a least one bit different since x != y
    ### let that bit be k-th bit, then we know on the k-th bit x ^ y = 1, let x be the
    ### one with 1 on k-th bit. Suppose we can find this k-th bit, then we can skip xoring
    ### y by checking if k bit mask * n == 0, and thus we would successfully transform the
    ### problem, we find k-th bit by getting x ^ y = bitmask and do bitmask ~ (-bitmask)
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for n in nums:
            bitmask ^= n
        k = bitmask & (-bitmask)
        result = [0, 0]
        for n in nums:
            if(k & n != 0):
                result[0] ^= n
        result[1] = bitmask ^ result[0]
        return result
