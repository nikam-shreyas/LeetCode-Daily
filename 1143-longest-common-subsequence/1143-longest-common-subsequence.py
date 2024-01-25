class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
#         l1 = len(text1)
#         l2 = len(text2)
#         dp = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        
#         def recurse(i, j):
#             if i<0 or j<0:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             if text1[i]==text2[j]:
#                 dp[i][j] = 1+recurse(i-1, j-1)
#             else:
#                 dp[i][j] = max(recurse(i-1, j), recurse(i, j-1))
#             return dp[i][j]
#         return recurse(l1-1, l2-1)
