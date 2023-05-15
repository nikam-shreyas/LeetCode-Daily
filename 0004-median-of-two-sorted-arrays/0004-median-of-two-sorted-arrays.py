class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArray = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                newArray.append(nums1[i])
                i+=1
            else:
                newArray.append(nums2[j])
                j+=1
                
        while i<m:
            newArray.append(nums1[i])
            i+=1
        while j<n:
            newArray.append(nums2[j])
            j+=1
        k = m+n
        if k%2==0:
            return (newArray[k//2-1]+newArray[k//2])/2
        else:
            return newArray[k//2]
        