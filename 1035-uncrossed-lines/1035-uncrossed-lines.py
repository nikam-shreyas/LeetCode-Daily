class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def recurse(i, j):            
            if i<0 or j<0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if nums1[i]==nums2[j]:
                dp[(i, j)] = 1+recurse(i-1, j-1)
            else:
                dp[(i, j)] = max(recurse(i, j-1), recurse(i-1, j))
            return dp[(i, j)]
        m = recurse(len(nums1)-1, len(nums2)-1)
        nums1.reverse()
        nums2.reverse()
        dp = {}
        m = max(m, recurse(len(nums1)-1, len(nums2)-1))
        return m
        