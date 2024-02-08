from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        h = [(-value, key) for key, value in counter.items()]
        heapify(h)
        ans = ""
        while h:
            value, key = heappop(h)
            value = -value
            ans+=key*value
        return ans