class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0, 0
        for n in nums:
            tmp = once
            once = (once ^ n) & (~twice)
            twice = ((twice ^ n) & tmp) | (twice & (~n))
        return once
    
    
    ### brute for all cases O(32)
    def singleNumber(self, nums):
        repeat = 3 # this can be arbitary as long as != target
        target = 1 # != repeat
        result = 0
        for i in range(32):
            count = 0
            for n in nums:
                bit = (n >> i) & 1
                count = (count + bit)
            if(count % 3):
                result |= (1 << i)
        ### This is needed in python because
        ### result would be casted into unsigned
        if(result >= (1 << 31)):
            result -= (1 << 32)
        return result
