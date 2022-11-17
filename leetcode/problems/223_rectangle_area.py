class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ans = 0
        ans += (ax2-ax1)*(ay2-ay1)
        ans += (bx2-bx1)*(by2-by1)
        
        overlap_x = max(min(ax2, bx2)-max(ax1, bx1), 0)
        overlap_y = max(min(ay2, by2)-max(ay1, by1), 0)
        ans -= (overlap_x * overlap_y)
        return ans
