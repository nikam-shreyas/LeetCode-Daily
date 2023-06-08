class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        i = 0
        j = cols-1
        count = 0
        while i<rows:
            while j>=0 and grid[i][j]<0:
                j-=1
            count+=cols-j-1
            i+=1
        return count