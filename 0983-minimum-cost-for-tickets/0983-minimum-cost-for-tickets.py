class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [inf for _ in range(days[-1]+1)]
        dp[0]=0
        # print(dp)
        for i in range(1, len(dp)):
            if i in days:
                if i>=1 and i>=7 and i>=30:
                    dp[i]=min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
                elif i>=1 and i>=7:
                    dp[i]=min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[0]+costs[2])
                elif i>=1:
                    dp[i]=min(dp[i-1]+costs[0], dp[0]+costs[1], dp[0]+costs[2])
            else:
                dp[i]=dp[i-1]
        # print(dp)
        return dp[days[-1]]