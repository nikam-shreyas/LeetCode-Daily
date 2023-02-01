class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        index = 0
        for i in range(len(prices)):
            ans = max(ans, prices[i]-prices[index])
            if prices[i]<prices[index]:
                index=i
        return ans