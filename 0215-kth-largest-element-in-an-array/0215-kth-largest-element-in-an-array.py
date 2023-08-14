class Solution:

      def findKthLargest(self, nums: List[int], k: int) -> int:

        # Initialize min and max values
        min_val = float('inf')  
        max_val = -float('inf')  

        # Find min and max in list
        for num in nums:
            max_val = max(max_val, num)
            min_val = min(min_val, num)

        # Create frequency list of size (max_val - min_val + 1)
        freq_list = [0 for _ in range(max_val - min_val + 1)]

        # Populate frequency list
        for num in nums:
            freq_list[num - min_val] += 1

        # Find kth largest by traversing frequency list backwards
        for i in range(len(freq_list)-1, -1, -1):
            k -= freq_list[i]  
            if k <= 0:
                return i + min_val

        return min_val