class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        # print(costs)
        while i<len(costs) and coins>=costs[i]:
            # print(coins, costs[i])
            coins-=costs[i]
            i+=1
        return i
            