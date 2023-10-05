class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = floor(len(nums)/3)
        ans = []
        for key, value in counter.items():
            if value>n:
                ans.append(key)
        return ans