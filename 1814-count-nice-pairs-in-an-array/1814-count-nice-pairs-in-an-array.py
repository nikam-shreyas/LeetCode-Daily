from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modu = pow(10, 9)+7
        def rev(num):
            ans = 0
            while num:
                ans=ans*10+num%10
                num//=10
            return ans
        num_rev = Counter([num - rev(num) for num in nums])
        ans = 0
        for key in num_rev.keys():
            n = num_rev[key]
            if n>=2:
                ans+=((n*(n-1))//2)
                ans=ans%modu
        return ans
        
        