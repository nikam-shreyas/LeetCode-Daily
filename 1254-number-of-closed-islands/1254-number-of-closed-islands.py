class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited= [[0 for i in range(cols)] for j in range(rows)]
        def area(x, y):
            if not (0<=x<rows and 0<=y<cols):
                return False
            elif grid[x][y] or visited[x][y]:
                return True
            else:
                visited[x][y]=1
                return all([area(x+1, y), area(x-1, y), area(x, y-1), area(x, y+1)])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0 and visited[i][j]==0 and area(i, j):
                    count+=1
        return count