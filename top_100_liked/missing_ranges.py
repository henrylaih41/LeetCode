class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        for n in nums:
            if(n-1 == lower):
                result.append(str(lower))
            elif(n-1 > lower):
                result.append(str(lower)+"->"+str(n-1))
            lower = n+1
        if(upper == lower):
            result.append(str(upper))
        elif(upper > lower):
            result.append(str(lower)+"->"+str(upper))
            
        return result
