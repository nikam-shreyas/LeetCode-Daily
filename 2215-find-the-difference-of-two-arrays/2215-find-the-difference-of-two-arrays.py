class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        s1 = nums1.difference(nums2)
        s2 = nums2.difference(nums1)
        return [list(s1), list(s2)]