class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        # Binary search loop: continue while the search range is valid
        while low <= high:
            mid = low + (high - low) // 2  # Calculate the middle index
            
            if nums[mid] == target:  # If the middle element is the target, return its index
                return mid
            
            if nums[low] <= nums[mid]:  # If the left half is in increasing order
                if nums[low] <= target < nums[mid]:  # If target is in the left half
                    high = mid - 1  # Update the high index to search the left half
                else:
                    low = mid + 1  # Update the low index to search the right half
            else:  # If the right half is in increasing order (and the left is rotated)
                if nums[mid] < target <= nums[high]:  # If target is in the right half
                    low = mid + 1  # Update the low index to search the right half
                else:
                    high = mid - 1  # Update the high index to search the left half
        
        return -1  # Target not found, return -1
