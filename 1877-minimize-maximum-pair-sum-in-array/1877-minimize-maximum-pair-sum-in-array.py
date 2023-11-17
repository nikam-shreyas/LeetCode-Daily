class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPair = -inf
        n = len(nums)
        for i in range(n//2):
            maxPair = max(maxPair, nums[i]+nums[n-1-i])
        return maxPair