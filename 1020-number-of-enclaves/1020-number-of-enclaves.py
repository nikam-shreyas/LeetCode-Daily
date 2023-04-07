class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def floodfill(i, j):
            if i<0 or j<0 or i>=r or j>=c:
                return
            if grid[i][j]==0:
                return
            grid[i][j]=2
            visited.add((i, j))
            for n in neighbors:
                nextx, nexty = n[0]+i, n[1]+j
                if (nextx, nexty) not in visited:
                    floodfill(nextx, nexty)
            return
        for i in range(r):
            floodfill(i, 0)
            floodfill(i, c-1)
        for j in range(c):
            floodfill(0, j)
            floodfill(r-1, j)
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    count+=1
        return count