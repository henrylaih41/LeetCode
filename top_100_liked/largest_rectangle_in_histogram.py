class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [(-1, -1)] # stack
        heights.append(-1) # dummy height
        maxx = 0
        for i, h in enumerate(heights):
            pt = i 
            while(h < s[-1][0]):
                    maxx = max(maxx, s[-1][0] * (i-s[-1][1]))
                    pt   = s[-1][1]
                    s.pop()
            s.append((h, pt))
        
        return maxx
