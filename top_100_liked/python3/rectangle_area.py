class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_area = self.calculate_area(ax2 - ax1, ay2 - ay1) 
        b_area = self.calculate_area(bx2 - bx1, by2 - by1)
        overlap = self.calculate_area(min(ax2, bx2) - max(ax1, bx1), min(by2, ay2) - max(by1, ay1))
        return a_area + b_area - overlap
    def calculate_area(self, w, h):
        
        return (w * h) if (w > 0 and h > 0) else 0
