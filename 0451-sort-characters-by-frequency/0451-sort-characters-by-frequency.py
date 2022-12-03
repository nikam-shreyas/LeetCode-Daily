from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        def sorting_key(element):
            key, value = element
            return -value
        counter = Counter(s)
        sorted_counter = sorted(counter.items(), key=sorting_key)
        ans = ['']
        for key, value in sorted_counter:
            ans.extend([key]*value)
        return ''.join(ans)