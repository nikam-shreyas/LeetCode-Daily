class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for i in range(c+1)] for j in range(r+1)]
        res = 0
        for i in range(r):
            for j in range(c):
                dp[i+1][j+1] = (min(dp[i][j], dp[i+1][j], dp[i][j+1])+1)*int(matrix[i][j])
                res = max(res, dp[i+1][j+1]**2)
        return res