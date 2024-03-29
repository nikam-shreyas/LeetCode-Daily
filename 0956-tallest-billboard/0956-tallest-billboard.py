class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(A):
            dp = {0: 0}
            for x in A:
                for d, y in dp.copy().items():
                    dp[d + x] = max(dp.get(x + d, 0), y)
                    dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
            return dp

        dp, dp2 = helper(rods[:len(rods) // 2]), helper(rods[len(rods) // 2:])
        return max(dp[d] + dp2[d] + d for d in dp if d in dp2)