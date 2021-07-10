class Solution:
    ### O(n)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return 0
        r, c, maxx = len(matrix), len(matrix[0]), 0
        h = [0] * c
        ### O(r) * O(c) = O(n)
        for i in range(r):
            ### O(c)
            for j in range(c):
                h[j] = 0 if int(matrix[i][j]) == 0 else int(matrix[i][j]) + h[j]
            ### O(c)
            maxx = max(maxx, self.largestRectangleArea(h))
        return maxx
  
    # O(len(heights)) = O(c)
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
