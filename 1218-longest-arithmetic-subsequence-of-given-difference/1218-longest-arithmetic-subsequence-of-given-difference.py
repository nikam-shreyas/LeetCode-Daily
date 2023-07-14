class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        
        dp = {arr[0]:1}
        maxval = 1
        
        for index in range(1, n):
            i = arr[index]
            if i-difference in dp:
                dp[i]=1+dp[i-difference]
                maxval = max(maxval, dp[i])
            else:
                dp[i]=1
                
        return maxval