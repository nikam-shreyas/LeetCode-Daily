class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0 
        j = 0
        glen = len(g)
        slen = len(s)
        count = 0
        while i<glen and j<slen:
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count