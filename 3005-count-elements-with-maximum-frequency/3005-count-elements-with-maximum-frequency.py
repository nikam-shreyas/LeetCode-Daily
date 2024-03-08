class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxkey = max(c.values())
        s = 0
        for k in c:
            if c[k]==maxkey:
                s+=c[k]
        return s