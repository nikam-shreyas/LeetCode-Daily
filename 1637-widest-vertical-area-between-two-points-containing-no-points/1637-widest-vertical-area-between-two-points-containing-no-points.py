class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxWidth = 0
        for i in range(1, len(points)):
            maxWidth = max(maxWidth, points[i][0]-points[i-1][0])
        return maxWidth