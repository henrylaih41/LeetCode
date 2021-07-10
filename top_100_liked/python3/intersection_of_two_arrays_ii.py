class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count, result = {}, []
        for n in nums1:
            count[n] = count.get(n, 0) + 1
        for n in nums2:
            if(count.get(n, 0) > 0):
                result.append(n)
                count[n] -= 1
            
        return result
