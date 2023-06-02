class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.count = 0
        self.mergeSort(nums)
        return self.count
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    self.count += len(left) - i
                    j += 1
                else:
                    i += 1
            nums[:] = sorted(nums)