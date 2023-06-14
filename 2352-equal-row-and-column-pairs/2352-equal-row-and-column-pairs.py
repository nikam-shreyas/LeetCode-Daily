class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                flag = False
                if grid[i][0]==grid[0][j]:
                    flag = True
                    for k in range(n):
                        if grid[i][k]!=grid[k][j]:
                            flag=False
                            break
                if flag:
                    count+=1
        return count
                    