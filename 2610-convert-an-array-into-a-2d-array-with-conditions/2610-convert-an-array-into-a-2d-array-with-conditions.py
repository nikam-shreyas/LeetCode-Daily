class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = Counter(nums)
        maxval = max(nums.values())
        ans = [[] for _ in range(maxval)]
        for k, v in nums.items():
            for j in range(v):
                ans[j].append(k)
        return ans
        