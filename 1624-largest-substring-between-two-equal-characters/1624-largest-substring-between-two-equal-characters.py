class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dp = {}
        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i>j or i>len(s) or j<0:
                dp[(i, j)] = -1
                return -1
            if s[i]==s[j]:
                dp[(i, j)] = j-i-1
                return j-i-1
            dp[(i, j)] = max(recurse(i+1, j), recurse(i, j-1))
            return dp[(i, j)]
        return recurse(0, len(s)-1)