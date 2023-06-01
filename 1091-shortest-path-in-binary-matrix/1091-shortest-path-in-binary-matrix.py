class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0,0)])
        if n==1 and grid[0][0]==0:
            return 1
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        neighbors = [[1, 1], [1, -1], [1, 0], [0, -1], [-1, -1], [0, 1], [-1, 1], [-1, 0]]
        dist = 1
        while queue:
            quelen = len(queue)
            for i in range(quelen):
                currx, curry = queue.popleft()
                for nx, ny in neighbors:
                    nnx = currx+nx
                    nny = curry+ny
                    if (nnx, nny)==(n-1, n-1):
                        return dist+1
                    if 0<=nnx<n and 0<=nny<n and grid[nnx][nny]==0:
                        queue.append((nnx, nny))
                        grid[nnx][nny]=1
            dist+=1
        return -1
        
                    