from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        if not trust and n==1:
            return n
        s = set()
        for x, y in trust:
            adj_list[y].append(x)
            s.add(x)
        for i in adj_list:
            if len(adj_list[i])==n-1 and i not in s:
                return i
        return -1
        
            