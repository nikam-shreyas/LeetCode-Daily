class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            
            if x not in UF:
                UF[x] = x
            if y not in UF:
                UF[y] = y
            rootX = find(x)
            rootY = find(y)
            UF[rootX] = rootY
        
        maxX = 10**4
        for x,y in stones:
            union(x,y+maxX)
        
        return len(stones) - len({find(n) for n in UF})