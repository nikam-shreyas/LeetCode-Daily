class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        i = 0
        removed = set()
        for j in range(len(nums) // 2, len(nums)):
            if nums[j] > nums[i] and i not in removed:
                removed.add(i)
                removed.add(j)
                i += 1
        return len(nums) - len(removed)
            