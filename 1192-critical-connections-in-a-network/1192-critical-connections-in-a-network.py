class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #1. discovery array -> first time the node was discovered
        #2. array closest neighbor with the monimum discovery time
        #3. lowest is the array of time of earliest discovered node reached from that node
        adj = defaultdict(list)
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)
        
        discovery = [-1 for _ in range(n)]
        lowest = [-1 for _ in range(n)]
        ans = []
        time = 0
        def dfs(curr, parent):
            nonlocal time
            if discovery[curr]!=-1:
                return
            lowest[curr]=time
            discovery[curr]=time
            time+=1
            for n in adj[curr]:
                if n==parent:
                    continue
                dfs(n, curr)
                if lowest[n]>discovery[curr]:
                    ans.append([n, curr])
                lowest[curr] = min(lowest[curr], lowest[n])
        
        dfs(0, 0)
        return ans
                    
            