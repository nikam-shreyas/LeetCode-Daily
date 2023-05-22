import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # O(n)
        freq = [(v, k) for k, v in counter.items()]
        heapq.heapify(freq) 
        return [x[1] for x in heapq.nlargest(k, freq)]
        