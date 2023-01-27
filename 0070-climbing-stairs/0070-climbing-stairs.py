class Solution:
    dp={0:1}
    
    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        elif n<0:
            return 0
        self.dp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dp[n]
        