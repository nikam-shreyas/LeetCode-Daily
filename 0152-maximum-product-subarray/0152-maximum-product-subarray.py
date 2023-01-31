class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=1
        r=1
        res = nums[0]
        for i in range(len(nums)):
            l=1 if l==0 else l
            r=1 if r==0 else r
            l=l*nums[i]
            r=r*nums[len(nums)-1-i]
            res=max(res, max(l,r))
        return res