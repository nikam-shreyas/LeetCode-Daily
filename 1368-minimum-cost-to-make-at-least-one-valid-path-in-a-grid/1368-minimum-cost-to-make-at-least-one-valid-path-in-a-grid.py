class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # (0, 0) just hold position, will not use, others for use of k later
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]         
        minHeap, visited = [], set()
        heappush(minHeap, (0, 0, 0))
        while minHeap:
            cost, x, y = heappop(minHeap)
            if (x, y) in visited: continue
            visited.add((x, y))
            if x == ROWS - 1 and y == COLS - 1:
                return cost
            for k in range(1, 5): # check 4 dirctions
                row = x + directions[k][0]
                col = y + directions[k][1]
                if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited: continue
                addNum = 0 if k == grid[x][y] else 1 # check whether need cost + 1
                heappush(minHeap, (cost + addNum, row, col))