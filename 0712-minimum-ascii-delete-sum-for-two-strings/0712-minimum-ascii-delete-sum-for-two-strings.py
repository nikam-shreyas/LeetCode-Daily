class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        dp = {}
        
        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i<0 and j<0:
                return 0
            
            if i<0:
                dp[(i, j)] = ord(s2[j])+recurse(i, j-1)
                
            elif j<0:
                dp[(i, j)] = ord(s1[i])+recurse(i-1, j)
                
            elif s1[i]==s2[j]:
                dp[(i, j)] = recurse(i-1, j-1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = min(
                    ord(s1[i])+recurse(i-1, j),
                    ord(s2[j])+recurse(i, j-1)
                )
                
            return dp[(i, j)]
        
        return recurse(len(s1)-1, len(s2)-1)