class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ay2-ay1)*(ax2-ax1)
        area_b = (by2-by1)*(bx2-bx1)
        x_common = min(ax2, bx2)-max(ax1, bx1)
        y_common = min(ay2, by2)-max(ay1, by1)
        common_area = 0
        if x_common>0 and y_common>0:
            common_area = x_common*y_common
        return area_a+area_b-common_area