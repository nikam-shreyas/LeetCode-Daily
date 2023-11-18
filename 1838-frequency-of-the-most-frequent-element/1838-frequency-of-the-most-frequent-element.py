class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        maxF = 1
        i = 0
        j = 1
        while i<len(nums)-1:
            while j<len(nums) and k>=nums[i]-nums[j]:
                k-=nums[i]-nums[j]
                j+=1
            maxF = max(maxF, j-i)
            if j==len(nums):
                break
            k+=(nums[i]-nums[i+1])*(j-i-1)
            i+=1
        return maxF