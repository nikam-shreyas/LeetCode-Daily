from heapq import heapify, heappop, heapreplace, nlargest, heappush
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = [-num*2 if num % 2 == 1 else -num for num in nums]
        heapq.heapify(pq)
        min_val = float('inf')
        for num in nums:
            min_val = min(min_val, num if num % 2 == 0 else num*2)
        min_deviation = float('inf')
        while True:
            max_val = -heapq.heappop(pq)
            min_deviation = min(min_deviation, max_val - min_val)
            if max_val % 2 == 1:
                break
            max_val //= 2
            min_val = min(min_val, max_val)
            heapq.heappush(pq, -max_val)
        return min_deviation