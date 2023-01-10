class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        count = 0
        prod = 1
        i = 0
        j = 0
        n = len(nums)
        while j<n:
            prod = 1
            while j<n and prod*nums[j]!=0:
                if prod>0:
                    count = max(count, j-i)
                prod*=(nums[j]/abs(nums[j]))
                j+=1
            while i<n and i<j:
                if prod>0:
                    count = max(count, j-i)
                prod/=(nums[i]/abs(nums[i]))
                i+=1
            j+=1
            i=j
        return count