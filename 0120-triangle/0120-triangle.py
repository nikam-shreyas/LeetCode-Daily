class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for row in range(1, rows):
            cols = len(triangle[row])
            for col in range(cols):
                left = max(0, col-1)
                curr = min(col, len(triangle[row-1])-1)
                triangle[row][col]+=min(triangle[row-1][left], triangle[row-1][curr])
        return min(triangle[rows-1])