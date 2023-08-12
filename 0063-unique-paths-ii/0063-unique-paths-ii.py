class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            if grid[i][0]==1:
                break
            dp[i][0]=1
        for j in range(c):
            if grid[0][j]==1:
                break
            dp[0][j]=1
        
        
        for i in range(1, r):
            for j in range(1, c):
                if grid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[r-1][c-1] if grid[r-1][c-1]==0 else 0