class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(2)] for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = max(nums[i-1], nums[i-1]+dp[i-1][1])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        return max(dp[-1][0], dp[-1][1])
#         def recurse(i, j):
#             if i>=n:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             if j:
#                 dp[i][j]=recurse(i+1, abs(j-1))
#             else:
#                 dp[i][j]=max(recurse(i+1, j), recurse(i+1, abs(j-1))+nums[i])
#             return dp[i][j]
#         return recurse(0, 0)

        
        