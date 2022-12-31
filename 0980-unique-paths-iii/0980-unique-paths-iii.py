class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j, visited):
            if 0<=i<rows and 0<=j<cols:
                if (i, j) in visited or grid[i][j]==-1:
                    return
                visited.add((i, j))
                # print(i, j, visited, len(visited), grid[i][j])
                if grid[i][j]==2:
                    if len(visited)==rows*cols:
                        self.count+=1
                    else:
                        return
                for x, y in neighbors:
                    dfs(i+x, j+y, visited.copy())
            
        visited = set()
        start_i = None
        start_j = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    start_i = i
                    start_j = j
                elif grid[i][j]==-1:
                    visited.add((i, j))
        dfs(start_i, start_j, visited)
        return self.count
                    
            
        
        