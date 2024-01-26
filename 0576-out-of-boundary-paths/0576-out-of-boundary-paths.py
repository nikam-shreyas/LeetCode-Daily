class Solution:
    def findPaths(self, m: int, n: int, maxMoves: int, startRow: int, startColumn: int) -> int:
        modu = pow(10, 9)+7
        # queue = deque([(startRow, startColumn)])
        # neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        # count = 0
        # for i in range(maxMoves):
        #     qlen = len(queue)
        #     for _ in range(qlen):
        #         cx, cy = queue.popleft()
        #         for nx, ny in neighbors:
        #             if 0<=cx+nx<m and 0<=cy+ny<n:
        #                 queue.append((cx+nx, cy+ny))
        #             else:
        #                 count=(count+1)%modu
        # return count
            
        self.count=0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dp = {}
        def recurse(i, j, rem_moves):
            if (i, j, rem_moves) in dp:
                return dp[(i, j, rem_moves)]
            if rem_moves<0:
                return 0
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            dp[(i, j, rem_moves)] = 0
            for nx, ny in neighbors:
                dp[(i, j, rem_moves)] += recurse(nx+i, ny+j, rem_moves-1)%modu
            return dp[(i, j, rem_moves)]
        return recurse(startRow, startColumn, maxMoves)%modu
        