class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanes(nums):
            cursum = nums[0]
            maxsum = nums[0]
            for i in range(1, len(nums)):
                if cursum<0:
                    cursum = 0
                cursum+=nums[i]
                maxsum = max(maxsum, cursum)
            return maxsum
        
        noncircularsum = kadanes(nums)
        totalsum = 0
        for i in range(len(nums)):
            totalsum+=nums[i]
            nums[i]=-nums[i]
        
        circularsum = totalsum + kadanes(nums)
        if circularsum==0:
            return noncircularsum
        return max(circularsum, noncircularsum)
                