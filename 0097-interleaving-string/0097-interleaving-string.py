class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        s3len = len(s3)
        dp = {}
        if s1len+s2len!=s3len:
            return False
        def recurse(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if k>=s3len:
                dp[(i, j, k)] = True
                return True
            if i<s1len and j<s2len:
                if s3[k]==s1[i] and s2[j]==s3[k]:
                    dp[(i, j, k)] =  recurse(i+1, j, k+1) or recurse(i, j+1, k+1)
                    return dp[(i, j, k)]
                elif s3[k]==s1[i]:
                    dp[(i, j, k)] = recurse(i+1, j, k+1)
                    return dp[(i, j, k)] 
                elif s3[k]==s2[j]:
                    dp[(i, j, k)] =  recurse(i, j+1, k+1)
                    return dp[(i, j, k)]
                else:
                    dp[(i, j, k)] = False
                    return False
            elif i<s1len:
                if s1[i]==s3[k]:
                    dp[(i, j, k)] =  recurse(i+1, j, k+1)
                    return dp[(i, j, k)] 
                else:
                    dp[(i, j, k)] = False
                    return False
            elif j<s2len:
                if s2[j]==s3[k]:
                    dp[(i, j, k)] = recurse(i, j+1, k+1)
                    return dp[(i, j, k)]
                else:
                    dp[(i, j, k)] = False
                    return False
            else:
                dp[(i, j, k)] = False
                return False
        return recurse(0, 0, 0)
                