from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = Counter(nums)
        largest = -1
        largest_num = -1
        for num in sorted(nums.keys()):
            if num%2==0:
                if nums[num]>largest:
                    largest = nums[num]
                    largest_num = num
        return largest_num