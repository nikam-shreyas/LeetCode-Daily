class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        left = [nums[0]]
        right = [nums[-1]]
        n = len(nums)
        
        for i in range(1, len(nums)):
            
            if nums[i]<left[-1]:
                left.append(nums[i])
            else:
                left.append(left[-1])
                
            if nums[n-1-i]>right[-1]:
                right.append(right[-1])
            else:
                right.append(nums[n-1-i])
                
        # print(left, right)
        right = list(reversed(right))
        
        minsum = inf
        for i in range(1, len(nums)-1):
            if left[i-1]<nums[i]>right[i+1]:
                minsum = min(minsum, left[i-1]+right[i+1]+nums[i])
            
        return minsum if minsum!=inf else -1
            
                
        
        