class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i<len(nums):
            if nums[i]==0:
                c = 0
                j=i
                while j<len(nums):
                    if nums[j]==0:
                        c+=1
                        j+=1
                    else:
                        break
                # print(c, j)
                count+=(c*(c+1))//2
                i=j-1
            i+=1
        return count
                        
        