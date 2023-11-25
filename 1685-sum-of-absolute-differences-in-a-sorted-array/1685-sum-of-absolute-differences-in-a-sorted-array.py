class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        n = len(nums)
        ans = [s-((n)*nums[0])]
        diff = 0
        snow = 0
        for i in range(1, len(nums)):
            temp = s
            snow+=nums[i-1]
            temp -= nums[i]*(n-i)
            cdiff = nums[i]-nums[i-1]
            diff+=cdiff*i
            ans.append(temp+diff-snow)
        return ans