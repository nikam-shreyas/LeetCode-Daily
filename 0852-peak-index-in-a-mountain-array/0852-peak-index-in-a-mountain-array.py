class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        n = len(arr)
        high = n-1
        while low<=high:
            mid = low+(high-low)//2
            if mid>0 and mid<n-1:
                if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                    return mid
                elif arr[mid-1]<arr[mid]:
                    low = mid
                else:
                    high = mid
        