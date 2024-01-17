from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # counter = Counter(arr)
        # s = set()
        # for key, value in counter.items():
        #     if value in s:
        #         return False
        #     else:
        #         s.add(value)
        # return True
        return all(val==1 for val in Counter(Counter(arr).values()).values())