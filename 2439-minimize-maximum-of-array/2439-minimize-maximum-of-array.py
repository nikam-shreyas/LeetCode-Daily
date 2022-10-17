class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum_ = 0
        res = 0
        for i in range(len(nums)):
            sum_+=nums[i]
            res = max(res, (sum_+i)//(i+1))
        return res