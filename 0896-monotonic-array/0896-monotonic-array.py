class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if nums[0]==nums[-1]:
            for i in range(1, len(nums)):
                if nums[i]!=nums[i-1]:
                    return False
            return True
        elif nums[0]<nums[-1]:
            for i in range(1, len(nums)):
                if nums[i-1]>nums[i]:
                    return False
            return True
        else:
            for i in range(1, len(nums)):
                if nums[i-1]<nums[i]:
                    return False
            return True