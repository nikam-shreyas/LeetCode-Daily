from collections import defaultdict
        
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjlist = defaultdict(list)
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        start = [0]
        visited = set()
        visited.add(0)
        # print(adjlist)
        def recurse(start, visited):
            # print(start)
            if not start:
                return 0
            curr = start.pop()
            temp = 0
            for n in adjlist[curr]:
                if n not in visited:
                    visited.add(n)
                    start.append(n)
                    temp += recurse(start, visited)
            # print(curr, start, temp)
            # print()
            if hasApple[curr] or temp>0:
                return 2+temp
            else:
                return 0
        ans = recurse(start, visited)
        return max(ans-2, 0)
                
        