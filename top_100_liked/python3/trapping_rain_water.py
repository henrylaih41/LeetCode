class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r, layer = 0, len(height)-1, 0
        while(l < r):
            olayer = layer
            layer = min(height[l], height[r])
            ans += (r-l+1)*(layer-olayer)
            if(height[l] <= height[r]):
                l, ans = self.find_max(ans, l, r, height, 1)
            else:
                r, ans = self.find_max(ans, r, l, height, -1)
        ans -= layer
        return ans
    ### pt = [0, len(height)-1]
    def find_max(self, ans, pt, pivot, height, dirr):
        maxx = height[pt]
        while( (pt != pivot) and height[pt] <= maxx):
            ans -= height[pt]
            pt += dirr
        return pt, ans
