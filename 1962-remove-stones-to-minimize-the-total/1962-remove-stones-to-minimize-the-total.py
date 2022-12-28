import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            curr = -heapq.heappop(piles)
            curr = curr-curr//2
            heapq.heappush(piles, -curr)
        return -sum(piles)
            
            