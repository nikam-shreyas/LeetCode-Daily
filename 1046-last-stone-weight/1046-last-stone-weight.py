from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones)>1:
            stone1 = -heappop(stones)
            stone2 = -heappop(stones)
            heappush(stones, -(stone1-stone2))
        return -heappop(stones)
            