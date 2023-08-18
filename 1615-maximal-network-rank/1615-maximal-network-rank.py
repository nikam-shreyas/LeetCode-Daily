class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        for start, end in roads:
            adj[start].add((start, end))
            adj[end].add((start, end))
        
        maxrank = 0
        # print(adj)
        for i in range(n-1):
            for j in range(i+1, n):
                # print(i, j)
                rank = len(adj[i].union(adj[j]))
                maxrank = max(maxrank, rank)
        return maxrank