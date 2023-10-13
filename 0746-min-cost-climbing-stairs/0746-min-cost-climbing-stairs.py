class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def recurse(step, currcost):
            if step in dp:
                return dp[step]
            if step>=len(cost):
                dp[step] = currcost
                return dp[step]
            dp[step] = min(recurse(step+1, currcost), recurse(step+2, currcost))+cost[step]
            return dp[step]
        return min(recurse(0, 0), recurse(1, 0))
        
        n = len(cost)
        dp = [cost[i] for i in range(n)]
        for i in range(2, n):
            dp[i] += min(dp[i-1, dp[i-2]])
        return dp[-1]
        