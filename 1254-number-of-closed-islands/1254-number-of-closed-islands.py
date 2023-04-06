class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def floodfill(row,col):
            
            if   row==0 or row==len(grid)   -1: aux = True
            elif col==0 or col==len(grid[0])-1: aux = True
            else: aux = False

            grid[row][col] = 1
            if(row > 0              and grid[row-1][col] == 0): aux += floodfill(row-1,col)
            if(row < len(grid)-1    and grid[row+1][col] == 0): aux += floodfill(row+1, col)
            if(col > 0              and grid[row][col-1] == 0): aux += floodfill(row,col-1)
            if(col < len(grid[0])-1 and grid[row][col+1] == 0): aux += floodfill(row, col+1)
            return aux

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0 and not floodfill(i,j)): res+=1
                    
        return res