from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        ans = []
        heapq.heapify(ans)
        for string in counts:
            count = counts[string]
            heapq.heappush(ans, (-count, string))
        res = []
        for i in range(k):
            res.append(heapq.heappop(ans)[1])
        return res