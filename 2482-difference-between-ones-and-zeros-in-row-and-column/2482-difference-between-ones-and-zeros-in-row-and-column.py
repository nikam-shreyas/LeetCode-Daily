class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        zerosRow = []
        onesCol = []
        zerosCol = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            onesRow.append(sum(grid[i]))
            zerosRow.append(n-onesRow[-1])
        for j in range(n):
            onesCol.append(sum([grid[k][j] for k in range(m)]))
            zerosCol.append(m-onesCol[-1])
        
        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j]=onesRow[i]+onesCol[j]-zerosRow[i]-zerosCol[j]
        return diff