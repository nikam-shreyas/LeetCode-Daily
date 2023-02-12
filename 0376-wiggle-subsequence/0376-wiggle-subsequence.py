class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1 for i in range(n)] for _ in range(2)]
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[0][i]=max(dp[1][j]+1, dp[0][i])
                elif nums[i]<nums[j]:
                    dp[1][i]=max(dp[0][j]+1, dp[1][i])
        # print(dp)
        return max(max(dp[0]),max(dp[1]))
                    