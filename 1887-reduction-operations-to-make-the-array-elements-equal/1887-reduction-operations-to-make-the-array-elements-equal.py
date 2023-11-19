from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        h = list(zip(counts.keys(), counts.values()))
        count = 0
        curr_count = 0
        keys = sorted(counts.keys(), reverse=True)[:-1]
        for key in keys:
            curr_count+=counts[key]
            count+=curr_count
        return count
            