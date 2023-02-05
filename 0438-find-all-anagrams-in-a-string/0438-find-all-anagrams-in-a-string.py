import heapq
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        p = sorted(p)
        ans = []
        for i in range(len(s)-len(p)+1):
            h2 = sorted(s[i:i+len(p)])
            if p==h2:
                ans.append(i)
        return ans