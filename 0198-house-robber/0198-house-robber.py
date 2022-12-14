class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        def recurse(i, j):
            if i>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j:
                dp[i][j]=recurse(i+1, abs(j-1))
            else:
                dp[i][j]=max(recurse(i+1, j), recurse(i+1, abs(j-1))+nums[i])
            return dp[i][j]
        return recurse(0, 0)
        