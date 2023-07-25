class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        
        low = 0
        high = n-1
        
        while low<high:
            # Binary Search
            mid = (high+low)//2         
            
            # Mountain peak condition
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            
            # Left slope, climb up right
            elif arr[mid-1]<arr[mid]:
                low = mid
            
            # Right slope, climb up left
            else:
                high = mid
        