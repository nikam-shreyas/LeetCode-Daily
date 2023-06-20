class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = 2*k+1
        if k == 0:
            return nums
        if n>len(nums):
            return [-1 for i in range(len(nums))]
        
        
        s = sum([nums[i] for i in range(n)])
        ans = []
        for i in range(k):
            ans.append(-1)
        ans.append(s//n)
        for i in range(k, len(nums)-k-1):
            s-=nums[i-k]
            s+=nums[i+k+1]
            ans.append(s//n)
            
        
        for i in range(k):
            ans.append(-1)
            
        return ans