class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        check = lambda a,b: 0 <= a < m and 0 <= b < n
        start = None
        allKeys = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] in  'abcdef':
                    allKeys += 1 << (ord(grid[x][y]) - ord('a'))
                if grid[x][y] == '@':
                    start = (x,y)
        queue = deque([(start[0], start[1], 0, 0)])
        visited = defaultdict(set)
        visited[0].add((start[0],start[1]))
        while queue:
            x, y, currKeys, currMoves = queue.popleft()
            for dx, dy in {(-1, 0), (1, 0), (0, 1), (0, -1)}:
                a, b = x + dx, y + dy
                if not check(a,b): continue
                if grid[a][b] == '#': continue
                if (a,b) in visited[currKeys]: continue
                if grid[a][b] in 'abcdef':
                    key = ord(grid[a][b]) - ord('a')
                    if (1 << key) & currKeys: continue
                    newKeys = currKeys | 1 << key
                    if newKeys == allKeys: return currMoves + 1
                    visited[newKeys].add((a,b))
                    queue.append((a, b, newKeys, currMoves + 1))
                elif grid[a][b] in 'ABCDEF':
                    key = ord(grid[a][b]) - ord('A')
                    if 1 << key & currKeys == 0: continue
                visited[currKeys].add((a,b))
                queue.append((a, b, currKeys, currMoves+1))
        return -1