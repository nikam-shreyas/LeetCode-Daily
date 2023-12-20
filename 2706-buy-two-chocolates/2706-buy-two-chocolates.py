class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = min(prices[0], prices[1])
        secondSmallest = max(prices[1], prices[0])
        for i in range(2, len(prices)):
            if prices[i]<secondSmallest:
                secondSmallest=prices[i]
            if prices[i]<smallest:
                secondSmallest = smallest
                smallest = prices[i]
        
        if smallest+secondSmallest<=money:
            return money-(smallest+secondSmallest)
        else:
            return money
        