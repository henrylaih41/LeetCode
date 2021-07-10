from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        head, tail = 0, len(height) - 1
        maxx = (tail - head) * min(height[head], height[tail])
        while(True):
            if(height[head] <= height[tail]):
                head = self.find_new(height, tail, head, 1)
            else:
                tail = self.find_new(height, head, tail, -1)
            print(head, tail)
            ### head tail met
            if((head == -1) or (tail == -1)):
                break
            maxx = max(maxx, (tail - head) * min(height[head], height[tail]))
        return maxx

    def find_new(self, height, st, pt, sign):
        print("find")
        old = height[pt]
        while(st != pt and height[pt] <= old):
            pt += sign
        if(pt == st):
            return -1
        print(pt)
        return pt

s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])
