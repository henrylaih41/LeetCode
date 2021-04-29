class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        self.d, self.cnt = {}, 0
        lists = [nums1, nums2, nums3, nums4]
        self.addHash(lists, 0, 0)
        self.countHash(lists, len(lists)//2, 0)
        return self.cnt
    
    def addHash(self, lists, i, value):
        if(i == len(lists)//2):
            self.d[value] = self.d.get(value, 0) + 1
        else:
            for v in lists[i]:
                self.addHash(lists, i+1, value+v)
    
    def countHash(self, lists, i, value):
        if(i == len(lists)):
            self.cnt += self.d.get(-value, 0)
        else:
            for v in lists[i]:
                self.countHash(lists, i+1, value+v)
