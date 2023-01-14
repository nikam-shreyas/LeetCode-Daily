
from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        m = defaultdict(str)
        for i in range(ord('a'), ord('z')+1):
            m[chr(i)]=chr(i)
            
        def find(x):
            corrections = []
            while x!=m[x]:
                corrections.append(m[x])
                x = m[x]
            return x, corrections
        
        def union(x, y):
            xp, c1 = find(x)
            yp, c2 = find(y)
            p = min(xp, yp)
            for i in c1:
                m[i] = p
            for j in c2:
                m[j] = p
            m[xp] = p
            m[yp] = p
            m[x] = p
            m[y] = p
        
        for x, y in zip(s1, s2):
            union(x, y)
            
        for x in m:
            p, _ = find(x)
            m[x] = p
        
        ans = []
        
        for i in baseStr:
            ans.append(m[i])
        return ''.join(ans)