from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for key, value in counter.items():
            if value in s:
                return False
            else:
                s.add(value)
        return True