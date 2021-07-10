class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums) == 0):
            return []
        head, result = nums[0], []
        for i in range(1, len(nums)):
            if(nums[i-1] == nums[i]-1):
                continue
            else:
                s = str(head)
                if(nums[i-1] != head):
                    s += ("->" + str(nums[i-1]))
                result.append(s)
                head = nums[i]
                          
        s = str(head)
        if(head != nums[-1]):
            s += ("->" + str(nums[-1]))
        result.append(s)
        return result
