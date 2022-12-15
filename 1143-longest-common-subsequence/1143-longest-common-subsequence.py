class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        
        def recurse(i, j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j] = 1+recurse(i-1, j-1)
            else:
                dp[i][j] = max(recurse(i-1, j), recurse(i, j-1))
            return dp[i][j]
        return recurse(l1-1, l2-1)