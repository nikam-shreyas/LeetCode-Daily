class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         dp[i, j] = min(dp[i-1, j], dp[i-1, j-1], dp[i-1, j+1])
#         dp[0, j] = matrix[0, j]
        n = len(matrix)
        dp =[[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                j1 = max(0, j-1)
                j2 = j
                j3 = min(n-1, j+1)
                dp[i][j] = matrix[i][j] + min(dp[i-1][j1], dp[i-1][j2], dp[i-1][j3])
        return min(dp[n-1])